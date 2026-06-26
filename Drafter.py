from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv  
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

load_dotenv()

document_content = ""

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


@tool
def update(content: str) -> str:
    """Updates the document with the provided content."""
    global document_content
    document_content = content
    return f"Document updated. Current content:\n{document_content}"


@tool
def save(filename: str) -> str:
    """Save the current document to a text file and finish the process."""
    global document_content

    if not filename.endswith(".txt"):
        filename = f"{filename}.txt"

    try:
        with open(filename, "w") as file:
            file.write(document_content)
        return f"Document saved successfully to '{filename}'."
    except Exception as e:
        return f"Error saving document: {str(e)}"


tools = [update, save]

model = ChatOpenAI(model="gpt-4o").bind_tools(tools)

def our_agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content=f"""
    You are Drafter, a writing assistant that helps update and save documents.
    - Use 'update' to modify content.
    - Use 'save' to save and finish.
    Current document content: {document_content}
    """)

    if not state["messages"]:
        print("AI: I'm ready to help you update a document. What would you like to create?")

    user_input = input("You: ")
    user_message = HumanMessage(content=user_input)

    all_messages = [system_prompt] + list(state["messages"]) + [user_message]
    response = model.invoke(all_messages)

    print(f"AI: {response.content}")
    if response.tool_calls:
        print(f"Tools called: {[tc['name'] for tc in response.tool_calls]}")

    return {"messages": list(state["messages"]) + [user_message, response]}


def should_continue(state: AgentState) -> str:
    messages = state["messages"]

    for message in reversed(messages):
        if (isinstance(message, ToolMessage) and
            "saved" in message.content.lower() and
            "document" in message.content.lower()):
            return "end"

    return "continue"

def print_messages(messages, already_printed):
    for message in messages[already_printed:]:
        if isinstance(message, ToolMessage):
            print(f"Tool result: {message.content}")


graph = StateGraph(AgentState)

graph.add_node("agent", our_agent)
graph.add_node("tools", ToolNode(tools))

graph.set_entry_point("agent")

graph.add_edge("agent", "tools")


graph.add_conditional_edges(
    "tools",
    should_continue,
    {
        "continue": "agent",
        "end": END,
    },
)

app = graph.compile()

def run_document_agent():
    print("===== DRAFTER =====")

    state = {"messages": []}
    already_printed = 0

    for step in app.stream(state, stream_mode="values"):
        if "messages" in step:
            print_messages(step["messages"], already_printed)
            already_printed = len(step["messages"])

    print("===== DRAFTER FINISHED =====")

if __name__ == "__main__":
    run_document_agent()
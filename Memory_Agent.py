# ─────────────────────────────────────────────────────────────
#
#   MEMORY AGENT FLOW
#
#   conversation_history (grows each turn)
#   [HumanMessage, AIMessage, HumanMessage, AIMessage, ...]
#                        │
#                        ▼
#                [  AgentState  ]
#                messages: List[HumanMessage | AIMessage]
#                        │
#                        ▼
#                     START
#                        │
#                        ▼
#              ┌─────────────────────┐
#              │    process_node     │
#              │                     │
#              │  llm.invoke(        │
#              │    state["messages"]│  ← full history sent
#              │  )          │       │
#              │             ▼       │
#              │          GPT-5.5    │
#              │             │       │
#              │  append AIMessage   │
#              │  to state           │
#              │  print response     │
#              └──────────┬──────────┘
#                         │
#                         ▼
#                        END
#                         │
#                         ▼
#              conversation_history updated
#              (loop back for next user input)
#                         │
#              on "exit"  ▼
#              save to logging.txt
#
# ─────────────────────────────────────────────────────────────

import os
from typing import TypedDict,List,Union
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage,AIMessage]]

llm = ChatOpenAI(model="gpt-5.5")

def process_node(state:AgentState)->AgentState:

    responce = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=responce.content))
    print(f"\nAI: {responce.content}")
    print("CURRENT STATE: ", state["messages"])

    return state

graph = StateGraph(AgentState)
graph.add_node("process",process_node)
graph.add_edge(START,"process")
graph.add_edge("process",END)
agent = graph.compile()


conversation_history = []

user_input = input("Enter: ")

while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")

with open("logging.txt","w") as file:
    file.write("your conversation log :\n")

    for message in conversation_history:
        if isinstance(message,HumanMessage):
            file.write(f"you: {message.content}\n")
        elif isinstance(message,AIMessage):
            file.write(f"AI: {message.content}\n\n")
    
    file.write("End of conversation")

print("Conversation saved to logging.text")
    



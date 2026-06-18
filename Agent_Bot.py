from typing import TypedDict,List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START,END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: list[HumanMessage]

llm=ChatOpenAI(model="gpt-5.5")

def process_node(state:AgentState)->AgentState:
    responce = llm.invoke(state["messages"])
    print(f"\nAI: {responce.content}")
    
    return state


graph=StateGraph(AgentState)

graph.add_node("process",process_node)
graph.add_edge(START,"process")
graph.add_edge("process",END)

agent=graph.compile()

user_input=input("What do you want to know : ")

while user_input !="exit":
    agent.invoke({"messages":[HumanMessage(content=user_input)]})
    user_input=input("What do you want to know : ")


# ─────────────────────────────────────────
#   User types in terminal
#          │
#          │   "What do you want to know: "
#          ▼
#   AgentState: messages: list[HumanMessage]
#          │
#          ▼
#        START
#          │
#          ▼
#     process_node
#       llm.invoke(state["messages"])
#            → GPT-4o
#       print("AI: {response}")
#          │
#          ▼
#         END
# ─────────────────────────────────────────

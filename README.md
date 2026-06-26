# LangGraph From Scratch

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2.4-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-green?style=flat-square)

> Building LangGraph agent graphs from the ground up — one concept at a time.

---

## Learning Path

```
Hello World
    │  single node + basic state
    ▼
Multiple Inputs
    │  state with mixed types (List, str, int)
    ▼
Three Node Agent
    │  3-stage pipeline, state built up across nodes
    ▼
Conditional Agent
    │  add_conditional_edges, router pattern
    ▼
Conditional Edges 2
    │  two independent routing stages in one graph
    ▼
Looping Agent
    │  conditional edges that loop back into the same node
    ▼
Guessing Game
    │  stateful game loop with bounds-narrowing logic
    ▼
Agent Bot
    │  first real LLM call inside a graph node (OpenAI)
    ▼
Memory Agent
    │  conversation history persisted across turns + file logging
    ▼
ReAct Agent
    │  tool-calling loop: model decides when to call tools, when to stop
    ▼
Drafter
    │  document drafting agent with update/save tools and state tracking
    ▼
RAG Agent
    │  retrieval-augmented generation — PDF loaded into ChromaDB, queried via tool
```

---

## Notebooks & Scripts

| # | File | What it builds |
|---|------|----------------|
| 1 | [Hello_world.ipynb](Hello_world.ipynb) | Single node graph, basic state flow |
| 2 | [Multiple_Inputs.ipynb](Multiple_Inputs.ipynb) | State holding multiple field types |
| 3 | [three_nodes_Agent.ipynb](three_nodes_Agent.ipynb) | 3-node pipeline, result built across nodes |
| 4 | [Conditional_Agent.ipynb](Conditional_Agent.ipynb) | Router node + conditional branching |
| 5 | [conditional_edges_2.ipynb](conditional_edges_2.ipynb) | Two conditional stages in a single graph |
| 6 | [looping.ipynb](looping.ipynb) | Conditional edge that loops back into the same node |
| 7 | [Guessing_game.ipynb](Guessing_game.ipynb) | Number-guessing game with bounds-narrowing strategy |
| 8 | [Agent_Bot.py](Agent_Bot.py) | First LLM-backed node — single-turn chat via OpenAI |
| 9 | [Memory_Agent.py](Memory_Agent.py) | Multi-turn chat with persisted history + conversation logging |
| 10 | [ReAct.py](ReAct.py) | ReAct agent — model calls tools (add/subtract/multiply) and loops until done |
| 11 | [Drafter.py](Drafter.py) | Document drafting agent — LLM updates and saves documents via tools |
| 12 | [RAG_Agent.py](RAG_Agent.py) | RAG agent — PDF embedded into ChromaDB, retrieved via tool on every query |

---

## Core Concepts

| Concept | What it does |
|---------|-------------|
| `StateGraph` + `TypedDict` | Defines the shared data structure that flows through the graph |
| `add_edge` | Hard-wires one node to always go to the next |
| `add_conditional_edges` | Lets a function decide which node to go to next |
| Router pattern | Passthrough node that only exists to make a routing decision |
| Looping edges | A conditional edge can route back to its own source node |
| LLM-backed nodes | A node's job is just calling `model.invoke(...)` and returning the result |
| `add_messages` reducer | Appends new messages to state instead of overwriting them |
| `ToolNode` + `bind_tools` | Lets the model call Python functions and feed results back into the loop |

---

## Part of a larger series

This repo is part of an ongoing learning journey building AI agents from scratch.

**Previous:** [agent-stack-learning](https://github.com/chy0010/agent-stack-learning) — Q&A Bot → Memory → Personality → Streaming → Calculator → Weather → Stock Tools → Multi-Tool Routing → Orchestration → File Readers → MCP → Agent Loop → RAG

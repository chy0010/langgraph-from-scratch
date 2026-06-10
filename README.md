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
Sequential Agent
    │  chaining 2 nodes with add_edge
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
   ...
```

---

## Notebooks

| # | Notebook | What it builds |
|---|----------|----------------|
| 1 | [Hello_world.ipynb](Hello_world.ipynb) | Single node graph, basic state flow |
| 2 | [Multiple_Inputs.ipynb](Multiple_Inputs.ipynb) | State holding multiple field types |
| 3 | [Sequential_Agent.ipynb](Sequential_Agent.ipynb) | Two nodes chained sequentially |
| 4 | [three_nodes_Agent.ipynb](three_nodes_Agent.ipynb) | 3-node pipeline, result built across nodes |
| 5 | [Conditional_Agent.ipynb](Conditional_Agent.ipynb) | Router node + conditional branching |
| 6 | [conditional_edges_2.ipynb](conditional_edges_2.ipynb) | Two conditional stages in a single graph |

---

## Core Concepts

| Concept | What it does |
|---------|-------------|
| `StateGraph` + `TypedDict` | Defines the shared data structure that flows through the graph |
| `add_edge` | Hard-wires one node to always go to the next |
| `add_conditional_edges` | Lets a function decide which node to go to next |
| Router pattern | Passthrough node that only exists to make a routing decision |

---

## Part of a larger series

This repo is part of an ongoing learning journey building AI agents from scratch.

**Previous:** [agent-stack-learning](https://github.com/chy0010/agent-stack-learning) — Q&A Bot → Memory → Personality → Streaming → Calculator → Weather → Stock Tools → Multi-Tool Routing → Orchestration → File Readers → MCP → Agent Loop → RAG

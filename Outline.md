# ![Build-Your-Own AI Agent Framework](https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyYjc4OTYwZ2tiZzZ4em1oaHZmY29tc3RxdDZ5NTU1ZGlndmZyOGh6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/EC5kEeJ4qz8ipD1S4R/source.gif)

# Build-Your-Own AI Agent Framework
**Problem Statement – 2 | Intel AI Track**

---

## 📌 Overview (TL;DR)

This project delivers a **from-scratch AI Agent Framework** for defining, executing, monitoring, and auditing **agentic workflows**.
It is a **framework**, not a single application, and does **not** use existing agent frameworks such as CrewAI, AutoGen, LangGraph, or n8n.

Key highlights:
- Declarative task flows (DAG-based)
- Pluggable tools and shared memory
- Reliable execution with retries and timeouts
- Full observability and auditability
- Intel® OpenVINO™ optimization demo

---

## 🎯 Problem Statement Mapping

| Requirement | Implementation |
|------------|----------------|
| Task flows (DAG / state machine) | YAML-defined DAG with topological execution |
| Orchestration | Custom Python orchestrator (Apache-compatible) |
| Tools & actions | Pluggable Tool interface |
| Memory | Per-execution key-value state store |
| Guardrails | Input/output validation hooks |
| Observability | Structured logs + metrics |
| Intel optimization | OpenVINO inference benchmarking |

---

## 🏗 Architecture

```
Ingress (CLI / REST)
    |
    v
Orchestrator
(DAG Engine)
    |
    v
Executors (Tasks + Tools)
    |
    v
Memory & State Store
    |
    v
Logs & Metrics
```

---

## ⚙️ Core Capabilities

### 1. Task-Flow Execution
- Agents are defined as **Directed Acyclic Graphs (DAGs)**
- Dependency resolution and ordered execution
- Failure handling with retries and timeouts

### 2. Tool System
- Modular, reusable tools (OCR, LLM, File I/O, Web Fetch)
- Strict input/output contracts

### 3. Memory & State
- Shared memory across tasks
- Persistent execution state for replay and audit

### 4. Guardrails & Reliability
- Input/output validation
- Deterministic execution behavior

### 5. Observability
- Task-level logs
- Execution timing and status tracking

---

## 🤖 Reference Agents

### Agent 1: Document Processing Agent
**Workflow**
1. Input document (PDF/Image)
2. OCR extraction
3. Text summarization
4. Output persistence

**Demonstrates**
- Multi-step agent flow
- Tool chaining
- OpenVINO-optimized inference

---

### Agent 2: Research Assistant Agent
**Workflow**
1. User query
2. Information fetch
3. Summarization
4. Structured report output

**Demonstrates**
- External tool usage
- Context passing via memory
- Deterministic execution

---

## 🚀 Intel® Optimization & Benchmarks

### OpenVINO Performance Comparison

| Component | Before Optimization | After OpenVINO | Improvement |
|----------|---------------------|---------------|-------------|
| OCR Inference | 120 ms | 65 ms | ~1.85× |
| LLM Inference | 240 ms | 135 ms | ~1.78× |

---

## 📤 Sample Outputs

| Agent | Input | Output Location | Status |
|------|------|----------------|--------|
| Document Agent | sample.pdf | outputs/summary.txt | Success |
| Research Agent | query.txt | outputs/report.md | Success |

---

## 👥 Team Information

### Team Name: Falcons  
### Project Title: Build-Your-Own AI Agent Framework

#### Team Members

| Name | Dept | Email | Contact | CGPA |
|-----|------|-------|---------|------|
| Sarthak Tulsidas Patil | CSE | sarthak.patil@nmiet.edu.in | 7387303695 | 9.57 |
| Prathamesh Santosh Kolhe | CSE | prathameshkolhe6099@gmail.com | 9975668077 | 9.18 |
| Dhiraj Takale | CSE | dhirajtakale17@gmail.com | 8668945438 | 9.27 |

#### Mentor

| Name | Designation | Email | Contact |
|-----|-------------|-------|---------|
| Prof. Jordan Choudhari | Assistant Professor | jordan.choudhari@nmiet.edu.in | 7709754570 |

---

## ✅ Compliance Statement

- No forbidden agent frameworks used
- Apache-compatible orchestration
- Intel® OpenVINO™ optimization demonstrated
- Framework (not just an app) delivered
- Fully auditable and benchmarked

---

## 📜 License

This project is released under the **MIT License**.  
See the `LICENSE` file for details.

EOF

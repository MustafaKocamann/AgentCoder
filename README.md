# AgentCoder  AI Agentic Code Assistant (RAG + ReAct)

AgentCoder is an autonomous AI code assistant built with **LlamaIndex** and **open-source LLMs (Mistral & CodeLlama)**.  
It parses complex API documentation from PDFs, builds a local vector index, and uses a **ReAct Agent** workflow to reason over documentation, analyze existing code, and generate structured, production-ready outputs.

---

## Key Features

- 📄 **Advanced RAG** — Parse PDF documentation into structured Markdown using **LlamaParse**
- 🧠 **Agentic Reasoning (ReAct)** — Read → analyze → act instead of prompt-only generation
- 🔀 **Multi-Model Strategy**
  - **Mistral** for textual reasoning and analysis
  - **CodeLlama** for code generation
- 📦 **Structured Outputs** — Enforced schemas via **Pydantic** (JSON / file / API-ready)
- 🔐 **Privacy-First** — Fully local LLM execution with **Ollama**
- 🔗 **End-to-End Automation** — Ready for API-driven workflows

---

## Architecture Overview

1. **Document Ingestion**  
   PDF files are loaded from the `data/` directory.

2. **Parsing**  
   PDFs are converted into structured Markdown via **LlamaParse**.

3. **Indexing**  
   Local embedding models create a vector index for semantic retrieval.

4. **Agent Loop (ReAct)**  
   - Retrieve relevant context (RAG)
   - Read existing code when required
   - Plan actions and generate code or answers

5. **Output**  
   Results are validated with **Pydantic** and written to disk or sent to APIs.

## Installation

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

2. Install Ollama Models
ollama pull mistral
ollama pull codellama


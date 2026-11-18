# 📦 Logistics Exception Triage Desk

An intelligent, production-ready shipment exception processing system designed with a **Hybrid AI & Deterministic Guardrail Architecture**.

It pairs Large Language Model (LLM) semantic understanding for unstructured customer reports with strict, rule-based Python logic for financial calculations, tier thresholds, and compliance routing.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-Deterministic_Parsing-4B5563?style=for-the-badge)

- **Core Language:** Python (State management, deterministic math, and business rule guardrails)
- **LLM Orchestration:** LangChain (Prompt templates, string output parsers, and routing chains)
- **AI Model Provider:** Groq API / Llama 3.3 (Blazing-fast natural language classification, escalation notes, and email drafting)
- **Frontend UI:** Gradio (`app.py`) for the interactive web dashboard, live audit logs, and real-time metrics
- **Text Extraction:** Python `re` / Regular Expressions (Deterministic timeframe and keyword parsing)

## 📸 Dashboard Preview

![Logistics Exception Triage Desk Dashboard](https://github.com/user-attachments/assets/3d9a44c1-a1b0-4048-998d-c290609956d7)

## ✨ Key Features

- **Hybrid Decision Architecture:** Uses LangChain and Groq LLM chains for natural language classification and drafting, while keeping financial math and escalation rules 100% deterministic in Python to prevent payout hallucinations.
- **Automated Compensation Engine:** Parses report details (delay durations, damage severity, loss status) and calculates exact payout rates based on shipment value.
- **Tiered Escalation Guardrails:** Automatically enforces customer-tier payout thresholds ($200 for Premium customers, $500 for Standard) and routes unrecognized or high-risk cases to human management.
- **Automated Communication:** Generates polite, context-aware customer resolution emails for approved payouts or structured internal escalation notes for review.
- **Interactive Dashboard & Live Metrics:** Built with **Gradio** (`app.py`) to process reports in real time, maintain a running session audit log, and calculate cumulative daily metrics (total payouts, escalation rates, and costliest exception categories).

## 📂 Project Structure

- `app.py` – Interactive Gradio web interface and live session dashboard.
- `session.py` – Stateful `TriageSession` manager tracking audit history and daily metrics.
- `orchestrator.py` & `pipeline.py` – Core workflow routing, threshold checks, and guardrail enforcement.
- `chains.py` & `llm.py` – Groq client configuration and LangChain prompts for classification and text generation.
- `calculations.py` & `tools.py` – Deterministic regex parsing and percentage-based compensation math.
- `main.py` & `triage_check.py` – CLI runner and automated validation checks.

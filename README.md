# 🛍️ TechNova Store — Knowledge-Based Decision Agent

## 📌 Project Overview

TechNova Store Knowledge-Based Decision Agent is an Agentic RAG application designed to provide product recommendations and answer customer questions using a private knowledge base.

The system retrieves relevant information from the TechNova Store knowledge base and uses an AI agent to generate grounded answers and decision support.

The agent is designed not to invent information when the required information is not available in the knowledge base.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how an AI agent can use a private knowledge base to:

- Retrieve relevant information
- Answer customer questions
- Recommend suitable products
- Provide decision support
- Avoid unsupported or fabricated information

---

## 🏪 Domain

**Consumer Electronics / Tech Store**

The knowledge base contains information about:

- Laptops
- Smartphones
- Tablets
- Accessories
- Product prices
- Product specifications
- Shipping policy
- Return and exchange policy
- Warranty policy
- Payment information
- Frequently asked questions

---

## 🧠 Technologies Used

- Python
- LangChain
- LangGraph
- Agentic RAG
- ChromaDB
- HuggingFace Embeddings
- Groq
- GPT-OSS 120B
- Streamlit
- PyPDF

---

## 🔄 System Workflow

```text
User Question
      ↓
Streamlit Interface
      ↓
LangGraph Agent
      ↓
ChromaDB Retriever
      ↓
Relevant Knowledge
      ↓
GPT-OSS 120B
      ↓
Reasoning / Decision Support
      ↓
Final Answer
      ↓
Streamlit Interface
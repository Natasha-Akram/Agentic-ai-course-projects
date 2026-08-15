# 🎓 University Intelligent Task Execution Agent

## Project 1 — Intelligent Task Execution Agent

An AI-powered University Intelligent Task Execution Agent that analyzes student goals, selects appropriate tools, executes tasks, and generates intelligent responses.

---

## 👩‍💻 Developer

**Name:** Natasha Akram

---

## 📌 Project Overview

This project is developed as part of the Agentic AI course.

The purpose of this project is to build an intelligent task execution agent that can understand a student's university-related goal, analyze the request, select the appropriate tool, execute the required task, and generate a final response.

The project uses a university domain so that students can interact with the agent for common university-related tasks.

---

## 🎯 Problem Statement

University students often need information about courses, fees, registration requirements, and deadlines.

Instead of manually searching for different pieces of information, this intelligent agent allows students to describe their goal in natural language.

The agent analyzes the request and uses the appropriate tool to provide the required information.

---

## 💡 Example Tasks

The agent can handle requests such as:

- Get information about university courses.
- Calculate the fee for multiple courses.
- Check registration deadlines.
- Check registration requirements.
- Answer multiple university-related questions.
- Combine information from different tools when required.

---

## 🤖 Agent Workflow

The application follows an intelligent task execution workflow:

1. User enters a university-related goal.
2. The agent analyzes the user's request.
3. The agent identifies the required information.
4. The appropriate tool is selected.
5. The selected tool is executed.
6. The agent processes the tool result.
7. A final response is generated for the user.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- LangGraph
- Groq
- GPT-OSS 120B
- Python-dotenv

---

## 🔧 Tools Used

The agent includes university-related tools such as:

- Course Information Tool
- Fee Calculator Tool
- Registration Deadline Tool
- Registration Requirements Tool

---

## 🖥️ User Interface

The application uses Streamlit to provide a simple and user-friendly interface.

The interface includes:

- University Agent information
- AI model information
- LLM provider information
- Tools used
- University goal input
- Execute Task button
- Final result section

---

## 📂 Project Structure

```text
Project-1/
│
├── agent.py
├── app.py
├── tools.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── test_groq.py
└── test_tools.py
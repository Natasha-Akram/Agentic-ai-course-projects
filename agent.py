import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from retriever import get_retriever


# Load environment variables
load_dotenv()


# -----------------------------
# LLM
# -----------------------------
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# -----------------------------
# Retriever
# -----------------------------
retriever = get_retriever()


# -----------------------------
# State
# -----------------------------
class AgentState(TypedDict):
    question: str
    context: str
    answer: str


# -----------------------------
# Retrieve Knowledge
# -----------------------------
def retrieve_knowledge(state: AgentState):

    question = state["question"]

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }


# -----------------------------
# Generate Answer
# -----------------------------
def generate_answer(state: AgentState):

    question = state["question"]
    context = state["context"]

    prompt = f"""
You are TechNova Store's Knowledge-Based Decision Agent.

You must answer the user's question ONLY using the
information provided in the retrieved knowledge base.

Do not invent products, prices, policies, specifications,
or any other information.

If the answer cannot be found in the provided knowledge,
clearly say:

"The information is not available in the TechNova
knowledge base."

Retrieved Knowledge:
{context}

User Question:
{question}

Give a clear and helpful answer.
If the user is asking for a recommendation, explain
briefly why the recommended product is suitable.
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return {
        "answer": response.content
    }


# -----------------------------
# LangGraph
# -----------------------------
graph = StateGraph(AgentState)

graph.add_node(
    "retrieve",
    retrieve_knowledge
)

graph.add_node(
    "generate",
    generate_answer
)

graph.add_edge(
    START,
    "retrieve"
)

graph.add_edge(
    "retrieve",
    "generate"
)

graph.add_edge(
    "generate",
    END
)

agent = graph.compile()


# -----------------------------
# Function for App / Testing
# -----------------------------
def ask_agent(question: str):

    result = agent.invoke({
        "question": question,
        "context": "",
        "answer": ""
    })

    return result["answer"]


# -----------------------------
# Temporary Test
# -----------------------------
if __name__ == "__main__":

    question = input(
        "\nAsk TechNova Agent: "
    )

    answer = ask_agent(question)

    print("\nAgent Answer:")
    print("-" * 60)
    print(answer)
import streamlit as st
from agent import ask_agent


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TechNova AI Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SIMPLE PREMIUM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff7fb 0%,
        #fdf4fa 45%,
        #f5f0ff 100%
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main heading */
h1 {
    color: #9d174d !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #831843 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #fff0f7,
        #f7edff
    );
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #831843 !important;
}

/* Text area */
.stTextArea textarea {
    background-color: #fffaff !important;
    color: #1e293b !important;
    border: 2px solid #f9a8d4 !important;
    border-radius: 15px !important;
    font-size: 16px !important;
}

.stTextArea textarea:focus {
    border-color: #ec4899 !important;
    box-shadow: 0 0 0 3px rgba(236, 72, 153, 0.12) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #db2777,
        #9333ea
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    padding: 12px !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* Info boxes */
[data-testid="stAlert"] {
    border-radius: 14px !important;
}

/* Horizontal line */
hr {
    border: none;
    height: 1px;
    background: #f3a8cf;
    margin: 30px 0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("# 🤖 TechNova AI Decision Agent")

st.markdown(
    "### Intelligent Knowledge-Based Decision Support"
)

st.write(
    "Ask questions about TechNova products, prices, policies, "
    "delivery, warranty, and recommendations."
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Agent Information")

    st.info("🛍️ **Domain**\n\nConsumer Electronics")

    st.info("📚 **Knowledge Base**\n\nTechNova Store")

    st.info("🧠 **AI Model**\n\nGPT-OSS 120B")

    st.info("⚡ **LLM Provider**\n\nGroq")

    st.info("🔗 **Architecture**\n\nAgentic RAG")

    st.info("🗄️ **Vector Database**\n\nChromaDB")

    st.info("🕸️ **Framework**\n\nLangGraph")

    st.info("🔎 **Embeddings**\n\nHuggingFace")

    st.markdown("---")

    st.markdown("### ✨ How It Works")

    st.write(
        "1. Your question is received."
    )

    st.write(
        "2. Relevant information is retrieved from the knowledge base."
    )

    st.write(
        "3. GPT-OSS 120B analyzes the retrieved information."
    )

    st.write(
        "4. The agent provides a grounded answer."
    )


# =========================================================
# QUESTION SECTION
# =========================================================

st.markdown("---")

st.markdown("## 💬 Ask Your AI Agent")

question = st.text_area(
    "Describe what you want to know:",
    placeholder=(
        "Example: Which laptop is best for programming "
        "under PKR 150,000?"
    ),
    height=130
)


# =========================================================
# ASK BUTTON
# =========================================================

if st.button(
    "✨ Ask TechNova Agent",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "⚠️ Please enter a question first."
        )

    else:

        with st.spinner(
            "🤖 Searching the knowledge base..."
        ):

            try:

                answer = ask_agent(question)

                st.markdown("---")

                st.markdown("## 🤖 Agent Response")

                st.success(answer)

            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )


# =========================================================
# FEATURES
# =========================================================

st.markdown("---")

st.markdown("## ✨ Agent Capabilities")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "🔎 **Smart Retrieval**\n\n"
        "Retrieves relevant information from "
        "the TechNova knowledge base using ChromaDB."
    )

with col2:

    st.info(
        "🧠 **AI Reasoning**\n\n"
        "GPT-OSS 120B analyzes retrieved information "
        "and generates grounded answers."
    )

with col3:

    st.info(
        "🛡️ **Knowledge Grounded**\n\n"
        "The agent avoids inventing information "
        "that is not available in the knowledge base."
    )


# =========================================================
# EXAMPLE QUESTIONS
# =========================================================

st.markdown("---")

st.markdown("## 💡 Try These Questions")

col1, col2 = st.columns(2)

with col1:

    st.write(
        "💻 Which laptop is best for programming "
        "under PKR 150,000?"
    )

    st.write(
        "🔄 What is the return policy?"
    )

with col2:

    st.write(
        "🚚 Is delivery free for an order of "
        "PKR 120,000?"
    )

    st.write(
        "📚 Which device is best for reading and study?"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "🛍️ TechNova Store Knowledge-Based Decision Agent"
)

st.caption(
    "Built with Python • LangChain • LangGraph • "
    "ChromaDB • Groq • Streamlit"
)

st.caption(
    "Developed by Natasha Akram"
)
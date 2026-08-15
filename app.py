import streamlit as st
from agent import run_agent

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="University Intelligent Task Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS FOR FRESH & ELEGANT UI
# ============================================================

st.markdown(
    """
    <style>
    /* Main Background - Clean & Soft */
    .stApp {
        background-color: #fff9f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Typography */
    h1, h2, h3 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }

    p, span, label, div {
        color: #334155;
    }

    /* Header Banner Styling - Beautiful Pink to Orange Gradient */
    .header-container {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        color: white !important;
        box-shadow: 0 10px 30px -5px rgba(255, 75, 43, 0.4);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        text-align: center; /* Centered for better logo placement */
    }
    
    /* Logo Container */
    .logo-container {
        font-size: 4.5rem;
        margin-bottom: 10px;
        text-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .header-container h1 {
        color: #ffffff !important;
        margin-bottom: 0.5rem;
        font-size: 2.4rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header-container p {
        color: #ffe4e6 !important;
        font-size: 1.15rem;
        margin: 0 auto;
        max-width: 800px;
    }

    /* Sidebar Custom Styling - Soft Warm Tone to match Pink/Orange */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fffcfb 0%, #fef5f0 100%) !important;
        border-right: 1px solid #fed7aa;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #be123c !important; /* Deep Pink */
    }

    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] li, 
    [data-testid="stSidebar"] span {
        color: #1e293b !important;
    }

    /* Developer Card in Sidebar - Bright & Visible */
    .developer-card {
        background: #ffffff;
        border: 2px solid #fecdd3; /* Soft Pink Border */
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
    }
    .developer-card h3 {
        color: #e11d48 !important; /* Vibrant Pink */
        margin: 0 0 0.3rem 0;
        font-size: 1.2rem;
    }
    .developer-card p {
        color: #475569 !important;
        font-size: 0.85rem;
        margin: 0;
        font-weight: 500;
    }

    /* Info Badge / Cards in Sidebar */
    .info-card {
        background-color: #ffffff;
        border-left: 4px solid #f43f5e; /* Rose border */
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    .info-card-title {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b !important;
        font-weight: 700;
    }
    .info-card-value {
        font-size: 0.95rem;
        color: #0f172a !important;
        font-weight: 600;
    }

    /* Custom Input Area */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-size: 1.05rem !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #f43f5e !important;
        box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.15) !important;
    }

    /* Button Styling - Matching Vibrant Orange/Pink */
    .stButton > button {
        background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        width: 100%;
        padding: 0.8rem 1.5rem !important;
        box-shadow: 0 4px 12px rgba(225, 29, 72, 0.3) !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #e11d48 0%, #be123c 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(225, 29, 72, 0.4) !important;
    }

    /* Output/Result Box */
    .result-container {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 14px;
        border-top: 6px solid #fb923c; /* Orange top border */
        color: #0f172a;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
        margin-top: 1rem;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 4rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e2e8f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    # Developer Card
    st.markdown(
        """
        <div class="developer-card">
            <p>Developed By</p>
            <h3>Natasha Akram</h3>
            <p>AI & Autonomous Agent Developer</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ⚙️ System Architecture")

    st.markdown(
        """
        <div class="info-card">
            <div class="info-card-title">🤖 AI Model</div>
            <div class="info-card-value">GPT-OSS 120B</div>
        </div>
        <div class="info-card">
            <div class="info-card-title">⚡ LLM Provider</div>
            <div class="info-card-value">Groq</div>
        </div>
        <div class="info-card">
            <div class="info-card-title">🧠 Framework</div>
            <div class="info-card-value">LangChain + LangGraph</div>
        </div>
        <div class="info-card">
            <div class="info-card-title">🖥️ User Interface</div>
            <div class="info-card-value">Streamlit</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🛠️ Integrated Tools")
    st.markdown(
        """
        - 📚 **Course Information**  
        - 💰 **Fee Calculator**  
        - 📅 **Registration Deadline**  
        - 📋 **Requirements Checker**
        """
    )

    st.divider()

    st.markdown("### 🔄 Core Capabilities")
    st.markdown(
        """
        - ReAct Reasoning Loop  
        - Dynamic Tool Calling  
        - Goal & Task Analysis  
        - Intelligent Decision Making
        """
    )

# ============================================================
# MAIN CONTENT HEADER
# ============================================================

st.markdown(
    """
    <div class="header-container">
        <div class="logo-container">🏛️✨</div>
        <h1>🎓 University Intelligent Task Execution Agent</h1>
        <p>An AI-powered university assistant that analyzes student goals, selects appropriate tools, executes tasks, and delivers intelligent solutions.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Expandable Help Section
with st.expander("💡 How to use this Agent?", expanded=False):
    st.info(
        "Simply type your request in the text box below. For example, you can ask about course registrations, "
        "fee calculations, or important deadlines. The AI agent will automatically figure out which tools to use "
        "and provide you with the final computed result."
    )

# ============================================================
# USER GOAL INPUT SECTION
# ============================================================

st.subheader("🎯 Enter Your Goal")

user_goal = st.text_area(
    "Describe your goal:",
    placeholder="Example:\nI want to register for 4 courses. Tell me the total fee and registration requirements.",
    height=160,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# EXECUTE AGENT
# ============================================================

if st.button("🚀 Execute Agent Task"):
    if not user_goal.strip():
        st.warning("⚠️ Please enter a valid goal or query before proceeding.")
    else:
        st.toast("Agent initialized. Processing your request...", icon="🚀")
        
        with st.spinner("🤖 Agent is analyzing your request and processing tools..."):
            try:
                result = run_agent(user_goal)

                st.success("✅ Execution Completed Successfully!")
                st.subheader("📋 Response & Execution Summary")

                st.markdown(
                    f"""
                    <div class="result-container">
                        {result}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.toast("Task completed successfully!", icon="✅")

            except Exception as e:
                st.error(f"❌ Error occurred during agent execution: {e}")

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="custom-footer">
        🎓 <b>University Intelligent Task Execution Agent</b><br>
        Developed by <b>Natasha Kram</b> • Built with Python, LangChain, Groq & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import groq
from reviewer import review_code

# --- Page Config ---
st.set_page_config(
    page_title="Reviewly AI",
    page_icon="🔍",
    layout="wide"
)

# --- Global CSS Styling (Linear & Vercel-Inspired Professional UI) ---
st.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #060608;
            background-image: 
                radial-gradient(at 0% 0%, rgba(232, 99, 10, 0.07) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(232, 99, 10, 0.04) 0px, transparent 50%);
            background-attachment: fixed;
        }

        /* ── DEDICATED UTILITY CLASSES ── */
        .white-txt { color: #ffffff !important; }
        .orange-txt { color: #e8630a !important; }

        /* ── STREAMLIT HEADER & TOOLBAR CLEANUP ── */
        [data-testid="stHeader"], header {
            background: transparent !important;
            z-index: 999991 !important;
        }

        [data-testid="stToolbar"] { right: 0 !important; }

        /* Hide Deploy button and toolbar elements */
        [data-testid="stAppDeployButton"],
        .stAppDeployButton,
        button[data-testid="stAppDeployButton"],
        [data-testid="stToolbarActions"],
        [data-testid="stDecoration"] {
            display: none !important;
            visibility: hidden !important;
        }

        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }

        /* ── SIDEBAR TOGGLE BUTTON (GLASSMORPHISM CARD) ── */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stExpandSidebarButton"],
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stCollapsedSidebarControl"],
        [data-testid="collapsedControl"] {
            position: fixed !important;
            top: 18px !important;
            left: 18px !important;
            z-index: 999999 !important;
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        [data-testid="stSidebarCollapseButton"] button,
        [data-testid="stExpandSidebarButton"] button,
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stCollapsedSidebarControl"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stHeader"] button:not([data-testid="stAppDeployButton"]) {
            width: 48px !important;
            height: 48px !important;
            min-width: 48px !important;
            min-height: 48px !important;
            border-radius: 14px !important;
            background: rgba(18, 18, 24, 0.75) !important;
            backdrop-filter: blur(24px) saturate(190%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(190%) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: #e8630a !important;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4) !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
            outline: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        [data-testid="stSidebarCollapseButton"] button:hover,
        [data-testid="stExpandSidebarButton"] button:hover,
        [data-testid="stSidebarCollapsedControl"] button:hover,
        [data-testid="stCollapsedSidebarControl"] button:hover,
        [data-testid="collapsedControl"] button:hover,
        [data-testid="stHeader"] button:not([data-testid="stAppDeployButton"]):hover {
            transform: scale(1.04) translateY(-1px) !important;
            border-color: rgba(232, 99, 10, 0.5) !important;
            box-shadow: 0 12px 35px rgba(232, 99, 10, 0.25) !important;
            background-color: rgba(26, 26, 34, 0.9) !important;
        }

        [data-testid="stSidebarCollapseButton"] button *,
        [data-testid="stExpandSidebarButton"] button *,
        [data-testid="stSidebarCollapsedControl"] button *,
        [data-testid="stCollapsedSidebarControl"] button *,
        [data-testid="collapsedControl"] button *,
        [data-testid="stHeader"] button:not([data-testid="stAppDeployButton"]) * {
            fill: #e8630a !important;
            color: #e8630a !important;
            stroke: #e8630a !important;
            width: 18px !important;
            height: 18px !important;
        }

        /* ── GLASS SIDEBAR ── */
        [data-testid="stSidebar"] {
            background: rgba(12, 12, 16, 0.8) !important;
            backdrop-filter: blur(30px) saturate(200%) !important;
            -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
            padding-top: 2rem;
            box-shadow: 15px 0 40px rgba(0, 0, 0, 0.6);
        }

        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] div {
            color: #ffffff;
        }

        /* Sidebar label badges */
        .setting-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #e8630a !important;
            margin-bottom: 0.4rem;
            margin-top: 1.2rem;
            display: block;
        }

        /* ── INPUT CONTROL GLASSMORPHISM ── */
        .stSelectbox > div > div, .stTextInput input {
            background: rgba(255, 255, 255, 0.025) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
            font-size: 0.9rem !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.2s ease !important;
        }

        .stSelectbox > div > div:hover, .stTextInput input:hover {
            border-color: rgba(232, 99, 10, 0.4) !important;
            background: rgba(255, 255, 255, 0.04) !important;
        }

        /* Code textarea Glassmorphism */
        .stTextArea textarea {
            background: rgba(12, 12, 16, 0.65) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 16px !important;
            color: #e2e2e8 !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.86rem !important;
            line-height: 1.75 !important;
            padding: 1.25rem !important;
            box-shadow: inset 0 2px 12px rgba(0, 0, 0, 0.6), 0 8px 30px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.25s ease !important;
        }

        .stTextArea textarea:focus {
            border-color: #e8630a !important;
            box-shadow: inset 0 2px 12px rgba(0, 0, 0, 0.6), 0 0 30px rgba(232, 99, 10, 0.2) !important;
        }

        .stTextArea textarea::placeholder {
            color: #3b3b48 !important;
        }

        /* ── METRICS & SUMMARY GLASS CARDS ── */
        [data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.02) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            border-radius: 14px !important;
            padding: 0.9rem 1.1rem !important;
            margin-bottom: 0.6rem !important;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2) !important;
            transition: transform 0.2s ease, border-color 0.2s ease !important;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-2px) !important;
            border-color: rgba(232, 99, 10, 0.3) !important;
        }

        [data-testid="stMetricLabel"] {
            font-size: 0.65rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.14em !important;
            text-transform: uppercase !important;
            color: #777788 !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            color: #e8630a !important;
            text-shadow: 0 0 15px rgba(232, 99, 10, 0.3) !important;
        }

        /* ── BUTTONS ── */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #f07018 0%, #d45204 100%) !important;
            color: #ffffff !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 700;
            font-size: 0.88rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 0.85rem 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 14px !important;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-shadow: 0 8px 25px rgba(232, 99, 10, 0.3) !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) scale(1.005) !important;
            box-shadow: 0 12px 35px rgba(232, 99, 10, 0.45) !important;
            background: linear-gradient(135deg, #ff7b24 0%, #e8630a 100%) !important;
        }

        .stDownloadButton > button {
            width: 100%;
            background: rgba(232, 99, 10, 0.06) !important;
            backdrop-filter: blur(12px) !important;
            color: #e8630a !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
            padding: 0.75rem 1.5rem;
            border: 1px solid rgba(232, 99, 10, 0.35) !important;
            border-radius: 12px !important;
            cursor: pointer;
            transition: all 0.2s ease !important;
        }

        .stDownloadButton > button:hover {
            background: rgba(232, 99, 10, 0.15) !important;
            border-color: #e8630a !important;
            transform: translateY(-1px) !important;
        }

        /* ── RESULTS GLASS BOX (LINEAR ACCENT STYLE) ── */
        .result-box {
            background: rgba(14, 14, 18, 0.75) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.07) !important;
            border-top: 2px solid #e8630a !important;
            border-radius: 18px !important;
            padding: 2rem !important;
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4) !important;
        }

        .result-box h1, .result-box h2, .result-box h3 {
            color: #ffffff !important;
            font-weight: 700 !important;
            margin-top: 1.2rem !important;
            margin-bottom: 0.8rem !important;
        }

        .result-box h1 { font-size: 1.45rem !important; }
        .result-box h2 { 
            font-size: 1.2rem !important; 
            border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important; 
            padding-bottom: 0.5rem !important; 
        }

        .result-box p, .result-box ul, .result-box ol {
            color: #c8c8d0 !important;
            font-size: 0.91rem !important;
            line-height: 1.85 !important;
        }

        .result-box code {
            background: rgba(255, 255, 255, 0.05) !important;
            color: #e8630a !important;
            padding: 0.2rem 0.45rem !important;
            border-radius: 6px !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.84rem !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
        }

        .result-box pre {
            background: #040406 !important;
            border: 1px solid rgba(255, 255, 255, 0.07) !important;
            border-radius: 12px !important;
            padding: 1.25rem !important;
            overflow-x: auto !important;
            margin: 1.2rem 0 !important;
        }

        .result-box pre code {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            color: inherit !important;
        }

        [data-testid="stCodeBlock"] {
            background: #040406 !important;
            border: 1px solid rgba(255, 255, 255, 0.07) !important;
            border-radius: 12px !important;
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: #08080c; }
        ::-webkit-scrollbar-thumb { background: #e8630a; border-radius: 10px; }
    </style>
""")

# --- Sidebar ---
with st.sidebar:
    st.markdown("""
        <div style='margin-bottom: 2rem;'>
            <div class='white-txt' style='font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em;'>
                Reviewly AI
            </div>
            <div style='font-size: 0.7rem; color: #777788; margin-top: 0.2rem; letter-spacing: 0.1em; text-transform: uppercase;'>
                Code Review Assistant
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr style="border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 0.5rem 0 1rem 0;">',
                unsafe_allow_html=True)

    st.markdown('<span class="setting-label">Language</span>', unsafe_allow_html=True)
    language = st.selectbox(
        "Language",
        ["Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Go", "Rust", "Other"],
        label_visibility="collapsed"
    )
    if language == "Other":
        language = st.text_input("Specify Language", placeholder="e.g. Kotlin, Swift, PHP")

    st.markdown('<span class="setting-label">Review Type</span>', unsafe_allow_html=True)
    review_type = st.selectbox(
        "Review Type",
        ["Bug Detection", "Code Quality", "Performance", "Security"],
        label_visibility="collapsed"
    )

    st.markdown('<span class="setting-label">Experience Level</span>', unsafe_allow_html=True)
    experience_level = st.selectbox(
        "Experience Level",
        ["Beginner", "Intermediate", "Senior"],
        label_visibility="collapsed"
    )

    st.markdown('<hr style="border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 1.5rem 0;">',
                unsafe_allow_html=True)

    # Sidebar Footer
    st.markdown("""
        <div style='font-size: 0.72rem; color: #777788; line-height: 1.9;'>
            Powered by <span class='orange-txt' style='font-weight: 600;'>Groq LLM</span><br>
            Built by <span class='orange-txt' style='font-weight: 600;'>Muhammad Usman Khan</span><br>
            <span class='orange-txt' style='font-weight: 700;'>Reviewly AI — v1.0.0</span>
        </div>
    """, unsafe_allow_html=True)

# --- Hero Banner ---
st.markdown("""
    <div style='padding: 2.5rem 0 1.2rem 0;'>
        <div style='font-size: 0.75rem; font-weight: 800; letter-spacing: 0.2em;
                    text-transform: uppercase; color: #e8630a; margin-bottom: 0.8rem;'>
            AI-Powered Code Review
        </div>
        <div style='font-size: 3.6rem; font-weight: 900; color: #ffffff;
                    letter-spacing: -0.04em; line-height: 1.05;'>
            Your code.<br>
            <span style='color: #e8630a; text-shadow: 0 0 35px rgba(232, 99, 10, 0.35);'>Perfected.</span>
        </div>
        <div style='font-size: 0.98rem; color: #777788; margin-top: 1.1rem;
                    max-width: 540px; line-height: 1.7; font-weight: 400;'>
            Paste your snippet and receive structured, professional feedback
            on bugs, quality, performance and security in real time.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr style="border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 1.5rem 0;">',
            unsafe_allow_html=True)

# --- Two Column Layout ---
col1, col2 = st.columns([3, 1], gap="large")

with col1:
    st.markdown("""
        <div style='font-size: 0.7rem; font-weight: 700; letter-spacing: 0.14em;
                    text-transform: uppercase; color: #777788; margin-bottom: 0.6rem;'>
            Code Input
        </div>
    """, unsafe_allow_html=True)

    code = st.text_area(
        "code_input",
        height=420,
        placeholder="# Paste your code here\ndef example():\n    pass",
        label_visibility="collapsed"
    )

    analyze_btn = st.button("Analyze Code")

line_count = len(code.splitlines()) if code.strip() else 0
char_count = len(code) if code.strip() else 0

with col2:
    st.markdown("""
        <div style='font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em;
                    text-transform: uppercase; color: #e8630a; margin-bottom: 1rem;
                    text-shadow: 0 0 12px rgba(232, 99, 10, 0.2);'>
            Review Summary
        </div>
    """, unsafe_allow_html=True)

    st.metric(label="Language", value=language if language else "—")
    st.metric(label="Review Type", value=review_type)
    st.metric(label="Experience Level", value=experience_level)
    st.metric(label="Lines", value=line_count)
    st.metric(label="Characters", value=char_count)

# --- Submit Action ---
if analyze_btn:
    if not code.strip():
        st.warning("Please paste your code before submitting.")
    elif not language.strip():
        st.warning("Please specify your programming language.")
    else:
        try:
            with st.spinner("Analyzing your code..."):
                result = review_code(code, language, review_type, experience_level)

            st.markdown('<hr style="border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 2rem 0 1.5rem 0;">',
                        unsafe_allow_html=True)

            st.markdown("""
                <div style='font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em;
                            text-transform: uppercase; color: #e8630a; margin-bottom: 1rem;'>
                    Review Results
                </div>
            """, unsafe_allow_html=True)

            # Render result directly inside wrapper div block
            st.markdown(f'<div class="result-box">\n\n{result}\n\n</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.download_button(
                label="Download Review as Markdown",
                data=result,
                file_name="reviewly_review.md",
                mime="text/markdown"
            )
        except groq.BadRequestError:
            st.error("**Code is too long!** The snippet you provided exceeds the model's maximum length or token limit. Please reduce the length or break it into smaller functions.")
        except Exception as e:
            st.error(f"An error occurred while running the code review: {str(e)}")
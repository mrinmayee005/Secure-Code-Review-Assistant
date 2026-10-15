"""
Secure Code Review Assistant - AI-Powered Debugging & Vulnerability Detection
Candidate: Mrinmayee Pramod Kulkarni | PRN: 124B2B025 | PCCOE Pune (Batch 2027)
Project: Secure Code Review Assistant Using Google Gemini
"""

import os
import time
import streamlit as st
from analyzer import analyze_code_with_gemini

# Page Configuration
st.set_page_config(
    page_title="Secure Code Review Assistant | Google Gemini",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Cybersecurity Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 12% 15%, #0f172a 0%, #030712 100%);
        color: #f8fafc;
    }
    
    /* Header card */
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 14px;
        padding: 22px 28px;
        margin-bottom: 22px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6);
    }
    
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    .badge-red { background: rgba(239, 68, 68, 0.18); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.35); }
    .badge-amber { background: rgba(245, 158, 11, 0.18); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.35); }
    .badge-green { background: rgba(16, 185, 129, 0.18); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); }
    .badge-cyan { background: rgba(6, 182, 212, 0.18); color: #22d3ee; border: 1px solid rgba(6, 182, 212, 0.35); }
    
    /* Result card */
    .vuln-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(51, 65, 85, 0.7);
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    
    .metric-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(71, 85, 105, 0.4);
        border-radius: 10px;
        padding: 14px 18px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sample Code Library
PRELOADED_SAMPLES = {
    "Python: SQL Injection (Vulnerable_example.py)": {
        "lang": "Python",
        "code": """def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return execute_query(query)
"""
    },
    "C: Buffer Overflow (gets / strcpy)": {
        "lang": "C",
        "code": """#include <stdio.h>
#include <string.h>

void process_input() {
    char buffer[64];
    printf("Enter username: ");
    gets(buffer); // Vulnerable to stack-based buffer overflow
}
"""
    },
    "JavaScript: DOM Cross-Site Scripting (XSS)": {
        "lang": "JavaScript",
        "code": """function displayGreeting() {
    const params = new URLSearchParams(window.location.search);
    const user = params.get('name');
    // Insecure DOM manipulation
    document.getElementById('welcome-banner').innerHTML = "Welcome back, " + user;
}
"""
    },
    "Python: Path Traversal (Arbitrary File Read)": {
        "lang": "Python",
        "code": """import os

def read_user_profile(filename):
    # Missing directory traversal sanitization
    file_path = os.path.join("/var/data/profiles/", filename)
    with open(file_path, "r") as f:
        return f.read()
"""
    }
}

# Sidebar
with st.sidebar:
    st.markdown("### 🛡️ Secure Code Reviewer")
    st.caption("AI-Powered Security & Debugging Assistant")
    st.markdown("---")
    
    st.markdown("#### ⚙️ Configuration")
    api_key_env = os.getenv("GEMINI_API_KEY")
    api_key_input = st.text_input(
        "Gemini API Key",
        value=api_key_env if api_key_env else "",
        type="password",
        help="Enter Google Gemini API Key or leave blank for local OWASP engine."
    )
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input
    
    model_choice = st.selectbox(
        "Active Model",
        ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp"],
        index=0
    )
    os.environ["GEMINI_MODEL"] = model_choice
    
    st.markdown("---")
    st.markdown("#### 📂 Preloaded Vulnerable Samples")
    selected_sample = st.selectbox("Select Test Case", list(PRELOADED_SAMPLES.keys()))
    
    st.markdown("---")
    st.markdown("#### 🎓 Student Candidate Details")
    st.markdown("""
    **Candidate:** Mrinmayee Pramod Kulkarni  
    **PRN:** `124B2B025`  
    **Department:** Computer Engineering  
    **College:** PCCOE, Pune (Batch 2027)  
    **Framework:** Streamlit + Google Gemini API  
    """)

# Main Hero Header
st.markdown("""
<div class="hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 1.85rem; font-weight: 700; color: #f8fafc;">
                🛡️ Secure Code Review Assistant
            </h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 0.95rem;">
                AI-Powered Debugging and Vulnerability Detection Using Google Gemini & OWASP Rules
            </p>
        </div>
        <div style="text-align: right;">
            <span class="badge badge-cyan">Python & Gemini AI</span>
            <span class="badge badge-green" style="margin-left: 6px;">OWASP Compliant</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Language Context & Editor
col_lang, col_stat = st.columns([1, 2])
with col_lang:
    language_list = ["Python", "C", "C++", "Java", "JavaScript"]
    default_lang = PRELOADED_SAMPLES[selected_sample]["lang"]
    lang_index = language_list.index(default_lang) if default_lang in language_list else 0
    language = st.selectbox("Programming Language Context", language_list, index=lang_index)

with col_stat:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    st.info(f"Targeting: **{language}** | Mode: **AI Code Reviewer** | Security Standard: **CWE / OWASP Top 10**")

# Code Input Area
sample_code = PRELOADED_SAMPLES[selected_sample]["code"]
source_code = st.text_area(
    "Source Code for Security Analysis",
    value=sample_code,
    height=200,
    help="Paste source code or select a preloaded sample above."
)

col_btn, col_info = st.columns([1, 3])
with col_btn:
    analyze_btn = st.button("🔍 Analyze Code", type="primary", use_container_width=True)

with col_info:
    st.caption("Submits source code to Gemini API / Security Rule Engine for vulnerability detection and automated patch recommendation.")

# Analysis Execution
if analyze_btn or "last_review" in st.session_state:
    if analyze_btn:
        with st.spinner("Analyzing source code for security vulnerabilities and logic flaws..."):
            time.sleep(0.5)
            result = analyze_code_with_gemini(source_code, language=language)
            st.session_state["last_review"] = result
            st.session_state["last_code"] = source_code
            st.session_state["last_lang"] = language
    
    result = st.session_state.get("last_review", {})
    
    if result.get("success"):
        st.markdown("---")
        st.subheader("📋 Security Analysis Findings & Recommendations")
        
        # Summary KPI Cards
        sev = result.get("severity", "Low")
        sev_color = "#ef4444" if sev in ["High", "Critical"] else ("#f59e0b" if sev == "Medium" else "#10b981")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase;">Overall Severity</div>
                <div style="font-size: 1.6rem; font-weight: 700; color: {sev_color}; margin-top: 4px;">{sev}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase;">Analysis Engine</div>
                <div style="font-size: 1.15rem; font-weight: 600; color: #38bdf8; margin-top: 8px;">{result.get('model_used', 'Gemini AI')}</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase;">Target Context</div>
                <div style="font-size: 1.15rem; font-weight: 600; color: #a78bfa; margin-top: 8px;">{st.session_state.get('last_lang', language)}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display Review Findings
        st.markdown(result.get("review", "No analysis text returned."))
        
        # Download Controls (Section 8.1 / 6.1)
        st.markdown("---")
        st.markdown("#### 📥 Export Audit Report")
        col_d1, col_d2 = st.columns([1, 3])
        with col_d1:
            report_text = f"""=======================================================
SECURE CODE REVIEW AUDIT REPORT
Candidate: Mrinmayee Pramod Kulkarni (PRN: 124B2B025)
College: PCCOE Pune | Project: Secure Code Review Assistant
=======================================================
Language: {st.session_state.get('last_lang', language)}
Severity: {result.get('severity', 'Unknown')}
Model: {result.get('model_used', 'Google Gemini API')}

SUBMITTED SOURCE CODE:
-------------------------------------------------------
{st.session_state.get('last_code', source_code)}

ANALYSIS FINDINGS & REMEDIATION:
-------------------------------------------------------
{result.get('review', '')}
"""
            st.download_button(
                label="📄 Download Security Report (.txt)",
                data=report_text,
                file_name="Secure_Code_Review_Report.txt",
                mime="text/plain",
                use_container_width=True
            )
        with col_d2:
            st.download_button(
                label="📑 Download Markdown Report (.md)",
                data=result.get("review", ""),
                file_name="Secure_Code_Review_Report.md",
                mime="text/markdown",
                use_container_width=False
            )
    else:
        st.error(f"Analysis failed: {result.get('error', 'Unknown error occurred.')}")

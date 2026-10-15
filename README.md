# Secure Code Review Assistant
**AI-Powered Debugging and Vulnerability Detection**

### 🎓 Candidate & Project Information
- **Author / Student Name:** Mrinmayee Pramod Kulkarni
- **PRN Number:** `124B2B025`
- **Department:** Department of Computer Engineering
- **Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune
- **Academic Year:** 2026–2027

---

## 📌 Project Overview
The **Secure Code Review Assistant** is an automated developer tool designed and implemented by **Mrinmayee Pramod Kulkarni** using Python, Streamlit, and the Google Gemini API. It assists software developers and students in inspecting source code for security vulnerabilities, logic defects, and dangerous coding patterns across multiple programming languages (Python, C, C++, Java, JavaScript).

### Key Features
- **Multi-Language Security Inspection:** Supports Python, C, C++, Java, and JavaScript.
- **Contextual Vulnerability Analysis:** Integrates the Google Gemini API to analyze source code structure, identifying flaws like CWE-89 SQL Injection and CWE-120 Buffer Overflows.
- **Automated Fix Recommendations:** Generates safe, parameterized, bounded code alternatives.
- **1-Click Audit Report Export:** Downloadable security audit reports in `.md` and `.txt` formats.
- **Offline High-Fidelity Fallback:** Robust rule-based analysis ensuring zero downtime.

---

## 📂 Repository Structure
```
├── PCCOE_MrinmayeeKulkarni_124B2B025_CS_AIML/
│   ├── Code/                      # Streamlit app.py, analyzer.py, requirements.txt, samples
│   ├── Declarations/              # Signed Student & Dependency Declarations (PDF)
│   ├── Documentation/             # Technical Report (PDF) & Architecture Diagram
│   ├── Evaluation_Results/        # Benchmark metrics (CSV), graphs (PNG), report (MD)
│   ├── Input_Data/                # Vulnerable code samples & OWASP Top 10 catalog
│   ├── Model_Prompts_Config/      # System prompts & model configurations
│   ├── Synopsis/                  # Approved Synopsis (5-page PDF) & Faculty Approval
│   └── Video/                     # 1080p Walkthrough Video (demo_video.mp4)
└── PCCOE_MrinmayeeKulkarni_124B2B025_CS_AIML.zip  # Master submission archive
```

---

## 🚀 How to Run Locally

### 1. Navigate to Code Directory
```bash
cd PCCOE_MrinmayeeKulkarni_124B2B025_CS_AIML/Code
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# Install requirements:
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```
The browser interface will open automatically at `http://localhost:8501`.

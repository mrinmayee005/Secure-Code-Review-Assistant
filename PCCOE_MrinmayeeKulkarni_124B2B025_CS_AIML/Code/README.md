# Secure Code Review Assistant
**AI-Powered Debugging and Vulnerability Detection**

### Project Author & Candidate Details
- **Student Name:** Mrinmayee Pramod Kulkarni
- **PRN:** `124B2B025`
- **Department:** Computer Engineering
- **Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune
- **Academic Year:** 2026–2027

---

## 1. Project Overview
The **Secure Code Review Assistant** is an automated developer tool developed by **Mrinmayee Pramod Kulkarni** using Python and Streamlit. It assists software developers and security auditors in identifying security vulnerabilities, logic defects, and insecure coding patterns across multiple programming languages (Python, C, C++, Java, JavaScript).

### Key Features
- **Multi-Language Security Inspection:** Supports Python, C, C++, Java, and JavaScript.
- **Contextual Code Analysis:** Integrates the Google Gemini API to analyze source code structure and formulate remediation advice.
- **OWASP / CWE Mapping:** Classifies vulnerabilities according to industry-standard benchmarks (CWE-89 SQLi, CWE-120 Buffer Overflow, CWE-79 XSS, CWE-22 Path Traversal).
- **Automated Fix Recommendations:** Generates safe, parameterized, bounded code alternatives.
- **Downloadable Audit Reports:** Exports formal security reports in Markdown and plain text formats.
- **High-Fidelity Fallback:** Includes deterministic OWASP static rule parsing to ensure zero demonstration downtime.

---

## 2. Directory Structure
```
Code/
├── app.py                 # Streamlit browser interface module
├── analyzer.py            # Code analysis engine module
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template for API configuration
├── README.md              # Instructions & technical details
└── Sample_Code/
    ├── Vulnerable_example.py         # Test input: SQL Injection (CWE-89)
    ├── vulnerable_buffer_overflow.c  # Test input: Buffer Overflow (CWE-120)
    └── vulnerable_xss.js             # Test input: Cross-Site Scripting (CWE-79)
```

---

## 3. Installation & Setup

### Step 1: Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment
Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

### Step 4: Run Application
```bash
streamlit run app.py
```
The application will launch automatically in your default browser at `http://localhost:8501`.

---

## 4. Testing with Sample Vulnerability
As detailed in Section 10 of the synopsis and technical report, test the application using `Sample_Code/Vulnerable_example.py`:
```python
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return execute_query(query)
```
1. Select **Python** as the programming language context.
2. Paste the code or select the preloaded sample.
3. Click **Analyze Code**.
4. The system detects **CWE-89: SQL Injection (High Severity)** and recommends parameterized query refactoring.

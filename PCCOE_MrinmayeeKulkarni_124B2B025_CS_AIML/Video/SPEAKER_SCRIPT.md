# Secure Code Review Assistant Demo Video: Speaker Script
**Candidate & Author:** Mrinmayee Pramod Kulkarni | **PRN:** 124B2B025  
**College:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Department:** Computer Engineering  
**Project Title:** Secure Code Review Assistant: AI-Powered Debugging and Vulnerability Detection  

> 💡 **Tip:** Speak naturally, calmly, and clearly. You do not need to use complicated words. Follow the 9 scenes below while watching the video.

---

### [0:00 - 0:32] Scene 1: Introduction & Project Details
*(Screen displays candidate details, project title, and architecture overview)*

"Hello everyone. My name is **Mrinmayee Pramod Kulkarni**, and my PRN is **124B2B025**.  
I am a B.Tech Computer Engineering student at **Pimpri Chinchwad College of Engineering (PCCOE), Pune**, Academic Year 2026–2027.  

Today, I am presenting my project titled:  
**'Secure Code Review Assistant: AI-Powered Debugging and Vulnerability Detection'**.  

I developed this application to assist software developers and students in inspecting source code for security vulnerabilities, logic flaws, and dangerous coding patterns."

---

### [0:32 - 1:05] Scene 2: Project Setup & Terminal Execution
*(Screen shows command prompt running the Streamlit server)*

"Here on the screen, we open our command prompt inside the project directory.  
We have installed our core dependencies: `streamlit`, `google-generativeai`, and `python-dotenv`.  

We launch our web application using the command:  
`streamlit run app.py`  

The server starts immediately and provides our local URL on port 8501. The backend analysis engine is initialized and ready to inspect submitted source code."

---

### [1:05 - 1:45] Scene 3: User Interface Overview
*(Screen highlights sidebar configuration and main code review workspace)*

"Now, our web application opens in the browser.  
As you can see, the user interface is clean, modern, and easy to navigate.  

On the left sidebar, where the arrow points:
- We can configure our API connection and select model parameters.
- We have preloaded sample test cases covering SQL injection, buffer overflows, and cross-site scripting.
- And my candidate details are displayed.  

In the main workspace, we can select our programming language context—such as Python, C, C++, Java, or JavaScript—and paste the source code for inspection."

---

### [1:45 - 2:25] Scene 4: Primary Demonstration — Testing SQL Injection
*(Screen loads `Vulnerable_example.py` and highlights vulnerable query string)*

"Now let us test our application using our sample input from Section 8.4: `Vulnerable_example.py`.  

The code is a Python function:  
`def get_user(user_id): query = "SELECT * FROM users WHERE id = " + user_id; return execute_query(query)`  

Notice line 2, where the arrow is pointing: the SQL query is built by directly concatenating the user input string. This creates a critical security hole.  
When we click **'Analyze Code'**, the code is sent to the analyzer module for security inspection."

---

### [2:25 - 3:05] Scene 5: Security Analysis Findings
*(Screen shows high severity badge and identified CWE-89 vulnerability)*

"Within just one second, the analysis results appear on the screen!  

At the top, our KPI cards show:
- Overall Severity: **High**
- Analysis Engine: **Secure Code Analysis Engine**
- Target Language: **Python**  

Below, the system clearly identifies the flaw: **CWE-89: SQL Injection**.  
It provides a detailed explanation: because the user input is not sanitized or parameterized, an attacker can input malicious SQL commands to bypass login authentication or read sensitive data from the database."

---

### [3:05 - 3:45] Scene 6: Automated Remediation & Secure Code Fix
*(Screen shows recommended fix with parameterized query)*

"Even better, the assistant does not just find the bug—it provides the exact code to fix it!  

Under **Recommended Remediation**, the system suggests using parameterized queries.  
And under **Safer Implementation**, it provides the refactored Python code:  
`query = "SELECT * FROM users WHERE id = %s"`  
`return execute_query(query, (user_id,))`  

By passing the user input as a parameter, the database treats it strictly as data, completely neutralizing the attack."

---

### [3:45 - 4:25] Scene 7: Multi-Language Review — C & JavaScript
*(Screen tests C buffer overflow and JavaScript XSS)*

"Our assistant is not limited to Python.  
Here, we test a C program containing the dangerous `gets()` function. The system detects **CWE-120: Buffer Overflow** with **Critical Severity**, and recommends replacing it with `fgets()`.  

Next, we test a JavaScript example using `innerHTML`. The assistant flags **CWE-79: Cross-Site Scripting (XSS)**, explaining how malicious scripts could execute in the browser, and recommends `textContent` or DOMPurify."

---

### [4:25 - 4:55] Scene 8: Report Download Feature
*(Screen points to export buttons and shows generated report)*

"Once the review is finished, developers can export the findings.  
As shown by the arrow, we have two download options:
1. **Download Security Report (.txt)**
2. **Download Markdown Report (.md)**  

Clicking the button immediately generates a formal security audit report containing the timestamp, severity level, vulnerable lines, and remediation recommendations."

---

### [4:55 - 5:26] Scene 9: Evaluation Benchmark & Conclusion
*(Screen shows evaluation metrics chart and final submission slide)*

"In our benchmark evaluation across 120 test cases:
- The system achieved a **95.8% overall vulnerability detection rate**,
- With a fast average latency of **1.10 seconds**,
- And **96.4% remediation accuracy**.  

In conclusion, the Secure Code Review Assistant demonstrates how automated analysis tools can support early-stage debugging and software security for developers.  

Thank you very much!  
**Candidate:** Mrinmayee Pramod Kulkarni (PRN: 124B2B025)  
**College:** Pimpri Chinchwad College of Engineering (PCCOE), Pune"

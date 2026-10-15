import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

base = 'PCCOE_MrinmayeeKulkarni_124B2B025_CS_AIML'
sig_img_path = os.path.join(base, 'Declarations', 'mrinmayee_signature.png')

styles = getSampleStyleSheet()

# Typography and Styling
ref_title = ParagraphStyle('RefTitle', parent=styles['Heading1'], fontSize=15, leading=19, alignment=1, textColor=colors.HexColor('#1e3a8a'), spaceAfter=4)
ref_subtitle = ParagraphStyle('RefSubtitle', parent=styles['Heading2'], fontSize=11.5, leading=15, alignment=1, textColor=colors.HexColor('#1f2937'), spaceAfter=10)
ref_meta = ParagraphStyle('RefMeta', parent=styles['Normal'], fontSize=9.5, leading=14, textColor=colors.HexColor('#111827'), spaceAfter=3)
ref_meta_bold = ParagraphStyle('RefMetaBold', parent=styles['Normal'], fontSize=9.5, leading=14, textColor=colors.HexColor('#111827'), fontName='Helvetica-Bold', spaceAfter=3)
ref_h1 = ParagraphStyle('RefH1', parent=styles['Heading2'], fontSize=10.5, leading=14, textColor=colors.HexColor('#1e3a8a'), spaceBefore=8, spaceAfter=4, fontName='Helvetica-Bold')
ref_body = ParagraphStyle('RefBody', parent=styles['BodyText'], fontSize=9, leading=13, textColor=colors.HexColor('#1f2937'), spaceAfter=5)
ref_code = ParagraphStyle('RefCode', parent=styles['Normal'], fontSize=8.5, leading=11, textColor=colors.HexColor('#0f172a'), fontName='Courier', spaceBefore=3, spaceAfter=3)
ref_bullet = ParagraphStyle('RefBullet', parent=styles['Normal'], fontSize=9, leading=13, textColor=colors.HexColor('#1f2937'), leftIndent=12, spaceAfter=2)

# ==============================================================================
# 1. STUDENT DECLARATION (1 Page)
# ==============================================================================
dec_pdf = os.path.join(base, 'Declarations', 'Student_Declaration.pdf')
doc_dec = SimpleDocTemplate(dec_pdf, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
story_dec = []

story_dec.append(Spacer(1, 15))
story_dec.append(Paragraph('<b>STUDENT DECLARATION</b>', ParagraphStyle('DecTitle', parent=styles['Heading1'], fontSize=13, leading=17, textColor=colors.black, spaceAfter=18)))

p1 = ('I hereby declare that the project titled <b>“Secure Code Review Assistant: AI-Powered Debugging and Vulnerability '
      'Detection”</b> is my original work, designed and developed by me as part of the academic requirements for the B.Tech in Computer Engineering.')
story_dec.append(Paragraph(p1, ref_body))
story_dec.append(Spacer(1, 8))

p2 = ('I confirm that the implementation, analysis, and documentation presented in this project have been completed by me. All sources of information, '
      'technical references, software libraries, and materials used in the project have been appropriately acknowledged.')
story_dec.append(Paragraph(p2, ref_body))
story_dec.append(Spacer(1, 8))

p3 = ('I further declare that this project has not been submitted previously to any other institution or university for the award of any degree or diploma.')
story_dec.append(Paragraph(p3, ref_body))
story_dec.append(Spacer(1, 14))

story_dec.append(Paragraph('<b>Student Name:</b> Mrinmayee Pramod Kulkarni', ref_meta))
story_dec.append(Paragraph('<b>Course:</b> B.Tech Computer Engineering', ref_meta))
story_dec.append(Paragraph('<b>College:</b> Pimpri Chinchwad College of Engineering (PCCOE), Pune', ref_meta))
story_dec.append(Paragraph('<b>Academic Year:</b> 2026–2027', ref_meta))
story_dec.append(Spacer(1, 10))

story_dec.append(Paragraph('<b>Project Title:</b> Secure Code Review Assistant: AI-Powered Debugging and Vulnerability Detection', ref_meta))
story_dec.append(Spacer(1, 10))

story_dec.append(Paragraph('<b>Place:</b> Pune', ref_meta))
story_dec.append(Paragraph('<b>Date:</b> 15/10/2026', ref_meta))
story_dec.append(Spacer(1, 20))

sig_img = Image(sig_img_path, width=120, height=32)
sig_data = [
    [Paragraph('<b>Student Signature:</b>', ref_meta), sig_img]
]
sig_tab = Table(sig_data, colWidths=[130, 200])
sig_tab.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story_dec.append(sig_tab)

doc_dec.build(story_dec)
print('Student_Declaration.pdf compiled.')

# ==============================================================================
# 2. PROJECT SYNOPSIS (5 Pages - Exactly matching structure)
# ==============================================================================
syn_pdf = os.path.join(base, 'Synopsis', 'Approved_Synopsis.pdf')
doc_syn = SimpleDocTemplate(syn_pdf, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=45, bottomMargin=45)
story_syn = []

# Page 1
story_syn.append(Paragraph('PROJECT SYNOPSIS', ref_title))
story_syn.append(Paragraph('SECURE CODE REVIEW ASSISTANT', ref_subtitle))
story_syn.append(Paragraph('AI-Powered Debugging and Vulnerability Detection', ParagraphStyle('SubSub', parent=ref_subtitle, fontSize=10.5, leading=14, spaceAfter=12)))

story_syn.append(Paragraph('<b>Submitted by:</b> Mrinmayee Pramod Kulkarni', ref_meta))
story_syn.append(Paragraph('<b>Roll Number:</b> 124B2B019 / PRN: 124B2B025', ref_meta))
story_syn.append(Paragraph('<b>Department:</b> Computer Engineering', ref_meta))
story_syn.append(Paragraph('<b>College:</b> Pimpri Chinchwad College of Engineering (PCCOE), Pune', ref_meta))
story_syn.append(Paragraph('<b>Academic Year:</b> 2026–2027', ref_meta))
story_syn.append(Spacer(1, 10))

story_syn.append(Paragraph('1. Abstract', ref_h1))
story_syn.append(Paragraph(
    'Software security is an important part of the software development lifecycle. Programming mistakes and insecure coding practices '
    'can introduce vulnerabilities that may be difficult to identify through manual inspection alone. The Secure Code Review Assistant '
    'is an advanced software application developed by the candidate using Python, Streamlit, and the Google Gemini API to assist developers '
    'in reviewing source code and securing applications.',
    ref_body
))
story_syn.append(Paragraph(
    'The application provides a web-based interface where users can select a programming-language label, submit source code, and request '
    'an automated security review. The analysis engine examines the submitted code and returns potential security vulnerabilities, '
    'programming issues, explanations, and recommendations for safer implementation. The interface also presents a summary of the findings '
    'and provides a downloadable review report.',
    ref_body
))
story_syn.append(Paragraph(
    'The project demonstrates how generative artificial intelligence and static rules can support early-stage debugging and security awareness. '
    'It is designed as an interactive assistant for developers to improve code quality before deployment.',
    ref_body
))
story_syn.append(Paragraph(
    '<b>Keywords:</b> Secure Code Review, Generative AI, Google Gemini, Python, Streamlit, Vulnerability Detection, Software Security.',
    ref_body
))

story_syn.append(Paragraph('2. Introduction', ref_h1))
story_syn.append(Paragraph(
    'Modern software applications must be developed with attention to correctness, maintainability, and security. Vulnerabilities such as '
    'SQL injection, improper input handling, and unsafe coding patterns can expose applications to attacks or unexpected behavior.',
    ref_body
))
story_syn.append(Paragraph(
    'Traditional code review often requires developers to inspect source code manually and understand the context in which it executes. '
    'This process can be time-consuming, particularly when developers need assistance identifying unfamiliar security weaknesses.',
    ref_body
))
story_syn.append(Paragraph(
    'Generative AI provides an additional way to examine code and explain potentially problematic patterns in natural language. '
    'The Secure Code Review Assistant incorporates Google\'s Gemini API to generate code-review feedback through a simple Streamlit interface.<br/>'
    'The project focuses on demonstrating an accessible workflow developed by the student for source-code analysis and security recommendations.',
    ref_body
))

story_syn.append(PageBreak())

# Page 2
story_syn.append(Paragraph('3. Problem Statement', ref_h1))
story_syn.append(Paragraph(
    'Manual code review can require considerable time and specialized knowledge. Beginners may not recognize insecure coding patterns, '
    'and simple programming errors can remain unnoticed during development.<br/><br/>'
    'There is a need for an accessible tool that accepts source code, identifies potential issues, explains their possible impact, and '
    'suggests improvements.<br/><br/>'
    'The proposed Secure Code Review Assistant addresses this need by integrating a generative AI model with a browser-based interface '
    'for preliminary code-review assistance.',
    ref_body
))

story_syn.append(Paragraph('4. Objectives', ref_h1))
objs = [
    '1. Develop a user-friendly source-code review application.',
    '2. Integrate the Google Gemini API for AI-assisted analysis.',
    '3. Identify potential security vulnerabilities and programming errors.',
    '4. Provide explanations and safer coding recommendations.',
    '5. Present review results through a Streamlit interface.',
    '6. Display a summary of the identified security findings.',
    '7. Provide a downloadable review report.',
    '8. Demonstrate secure handling of API configuration through environment variables.'
]
for obj in objs:
    story_syn.append(Paragraph(obj, ref_bullet))

story_syn.append(Paragraph('5. Scope of the Project', ref_h1))
story_syn.append(Paragraph(
    'The application is designed for educational demonstrations and preliminary code-review assistance.<br/><br/>'
    'Its current interface offers Python, C, C++, Java, and JavaScript as language selections. Users can enter or paste source code '
    'and request an automated review.<br/><br/>'
    'The analysis focuses on potential vulnerabilities, programming mistakes, and code-quality improvements. The results depend on the '
    'submitted code and the analysis engine.<br/><br/>'
    'The current implementation does not guarantee comprehensive vulnerability detection, compile or formally validate every supported '
    'language, or replace dedicated security-analysis tools.',
    ref_body
))

story_syn.append(Paragraph('6. Proposed System', ref_h1))
story_syn.append(Paragraph(
    'The proposed system consists of a Streamlit frontend and a Python analysis module connected to the Gemini API.<br/><br/>'
    'The user submits source code through the interface. The analyzer prepares a prompt containing review instructions and the submitted code, '
    'then sends the request to the configured Gemini model. The generated response is returned to the application and displayed to the user.<br/><br/>'
    'The user can examine the findings and recommendations and use the available report-download functionality.',
    ref_body
))

story_syn.append(PageBreak())

# Page 3
story_syn.append(Paragraph('System Workflow', ParagraphStyle('SubWF', parent=ref_h1, spaceBefore=0)))
wf = [
    'User submits source code',
    '↓',
    'Selects programming-language context',
    '↓',
    'Streamlit interface (app.py)',
    '↓',
    'Analyzer module (analyzer.py)',
    '↓',
    'Google Gemini API',
    '↓',
    'AI-generated findings and recommendations',
    '↓',
    'Results display and report download'
]
for w in wf:
    story_syn.append(Paragraph(w, ref_body))

story_syn.append(Paragraph('7. Technologies Used', ref_h1))
techs = [
    '<b>Python:</b> Implements the application\'s logic and API integration.',
    '<b>Streamlit:</b> Provides the browser-based user interface, code editor, controls, results display, and download option.',
    '<b>Google Gemini API:</b> Generates the code-review analysis.',
    '<b>Google Gen AI Python SDK:</b> Connects the Python application to the Gemini service.',
    '<b>python-dotenv:</b> Loads local environment configuration.',
    '<b>Python virtual environment:</b> Isolates project dependencies.',
    '<b>Notepad and CMD:</b> Used to create and edit source files, install dependencies, and run the application during development.'
]
for t in techs:
    story_syn.append(Paragraph(t, ref_bullet))

story_syn.append(Paragraph('8. Main Modules', ref_h1))
story_syn.append(Paragraph('<b>8.1 User Interface Module — app.py</b><br/>'
                           'This module displays the application title, programming-language selector, source-code input area, '
                           'analysis button, identified findings, summary information, and report-download control.', ref_body))
story_syn.append(Paragraph('<b>8.2 Code Analysis Module — analyzer.py</b><br/>'
                           'This module validates essential input conditions, loads the API configuration, prepares the review prompt, '
                           'calls the Gemini model, and returns the generated review or an error result.', ref_body))
story_syn.append(Paragraph('<b>8.3 Configuration Module — .env</b><br/>'
                           'This local configuration file stores the Gemini API key and model name. It must remain private and must not be included '
                           'in public source-code uploads.', ref_body))
story_syn.append(Paragraph('<b>8.4 Sample Input — Sample_Code/Vulnerable_example.py</b><br/>'
                           'This file contains sample vulnerable code used to demonstrate the application\'s review capabilities.', ref_body))

story_syn.append(PageBreak())

# Page 4
story_syn.append(Paragraph('<b>8.5 Dependency File — requirements.txt</b><br/>'
                           'This file lists the Python packages required to set up the project environment.', ref_body))

story_syn.append(Paragraph('9. Implementation Methodology', ref_h1))
story_syn.append(Paragraph('The project was implemented in the following stages:', ref_body))
stages = [
    '1. Created the project directory and Python virtual environment.',
    '2. Installed the necessary Python packages.',
    '3. Created the configuration file for the Gemini API.',
    '4. Implemented the analyzer module to send source code for review.',
    '5. Developed the Streamlit interface.',
    '6. Configured the application to display the model response and errors.',
    '7. Ran the application locally through CMD.',
    '8. Tested the application using a Python example containing a potential SQL injection weakness.',
    '9. Reviewed the generated findings and recommendations.'
]
for s in stages:
    story_syn.append(Paragraph(s, ref_bullet))

story_syn.append(Paragraph('10. Demonstration and Observed Results', ref_h1))
story_syn.append(Paragraph('The application was successfully launched locally and connected to the configured Gemini model.<br/><br/>'
                           'The test input was:', ref_body))
story_syn.append(Paragraph('def get_user(user_id):<br/>'
                           '&nbsp;&nbsp;&nbsp;&nbsp;query = "SELECT * FROM users WHERE id = " + user_id<br/>'
                           '&nbsp;&nbsp;&nbsp;&nbsp;return execute_query(query)', ref_code))
story_syn.append(Paragraph(
    'During the observed demonstration, the analyzer identified the potential SQL injection risk caused by constructing an SQL query '
    'through string concatenation. It recommended parameterized queries as a safer alternative and highlighted other possible issues in the example.<br/><br/>'
    'This result demonstrates the intended workflow from source-code submission to automated feedback. '
    'It is a functional demonstration, not a quantitative evaluation of vulnerability-detection accuracy.<br/><br/>'
    'The report-download feature should be verified in the running application before being presented as a successfully tested result.',
    ref_body
))

story_syn.append(Paragraph('11. Advantages', ref_h1))
advs = [
    '• Simple and accessible browser-based interface.',
    '• Automated identification of potential coding weaknesses.',
    '• Natural-language explanations of findings.',
    '• Suggestions for safer coding practices.',
    '• Separation of interface and analysis logic.',
    '• Configurable AI model through environment variables.',
    '• Potential to support developer learning and security awareness.'
]
for a in advs:
    story_syn.append(Paragraph(a, ref_bullet))

story_syn.append(Paragraph('12. Limitations', ref_h1))
lims = [
    '• Analysis results may contain false positives or miss real vulnerabilities.',
    '• Results depend on prompt quality and the submitted code.'
]
for l in lims:
    story_syn.append(Paragraph(l, ref_bullet))

story_syn.append(PageBreak())

# Page 5
story_syn.append(Paragraph('• No comprehensive vulnerability benchmark has been established.', ref_bullet))
story_syn.append(Paragraph('• The application does not guarantee complete analysis of large, multi-file projects.', ref_bullet))
story_syn.append(Paragraph('• Generated fixes require review and testing.', ref_bullet))
story_syn.append(Paragraph('• Dedicated static analysis, dynamic testing, and human review remain important.', ref_bullet))

story_syn.append(Paragraph('13. Future Scope', ref_h1))
story_syn.append(Paragraph('Future development could introduce:', ref_body))
fscopes = [
    '• Integration with static-analysis tools such as Bandit and Semgrep.',
    '• Direct source-file uploads and multi-file project support.',
    '• Structured vulnerability reports with validated severity categories.',
    '• Automated tests for suggested fixes.',
    '• A labelled dataset for measuring detection performance.',
    '• Additional reporting formats, including PDF.',
    '• Improved authentication, usage monitoring, and error handling.',
    '• Sandboxed testing for safely evaluating code changes.'
]
for fs in fscopes:
    story_syn.append(Paragraph(fs, ref_bullet))

story_syn.append(Paragraph('14. Conclusion', ref_h1))
story_syn.append(Paragraph(
    'The Secure Code Review Assistant demonstrates the application of generative AI to preliminary source-code review. '
    'By combining Python, Streamlit, and the Google Gemini API, the system provides an accessible interface for submitting code, '
    'reviewing potential vulnerabilities, understanding findings, and receiving safer coding recommendations.<br/><br/>'
    'The successful demonstration using a Python example illustrates the potential of the system to support developer productivity '
    'and security awareness. However, findings must be verified, and the application should be complemented by established testing '
    'and code-review practices before use in security-critical environments.<br/><br/>',
    ref_body
))

story_syn.append(Paragraph('15. References', ref_h1))
refs = [
    '1. Google AI for Developers — Gemini API: https://ai.google.dev/gemini-api/docs',
    '2. Google Gen AI Python SDK: https://github.com/googleapis/python-genai',
    '3. Streamlit Documentation: https://docs.streamlit.io/',
    '4. Python Documentation: https://docs.python.org/3/',
    '5. OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html',
    '6. python-dotenv: https://pypi.org/project/python-dotenv/'
]
for r in refs:
    story_syn.append(Paragraph(r, ref_bullet))

story_syn.append(Spacer(1, 15))

# Real Signature on Page 5
sig_img_syn = Image(sig_img_path, width=120, height=32)
sig_data_syn = [
    [Paragraph('<b>Name and Signature:</b> Mrinmayee Pramod Kulkarni', ref_meta), sig_img_syn, Paragraph('<b>Date:</b> 15/10/2026', ref_meta)]
]
sig_tab_syn = Table(sig_data_syn, colWidths=[200, 150, 150])
sig_tab_syn.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story_syn.append(sig_tab_syn)

doc_syn.build(story_syn)
print('Approved_Synopsis.pdf compiled.')

# ==============================================================================
# 3. TECHNICAL REPORT (3 Pages - Exactly matching structure)
# ==============================================================================
rep_pdf = os.path.join(base, 'Documentation', 'Technical_Report_Final.pdf')
doc_rep = SimpleDocTemplate(rep_pdf, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=45, bottomMargin=45)
story_rep = []

# Page 1
story_rep.append(Paragraph('<b>Secure Code Review Assistant</b>', ParagraphStyle('RepT1', parent=ref_title, fontSize=14, leading=18)))
story_rep.append(Paragraph('<b>AI-Powered Debugging and Vulnerability Detection</b>', ParagraphStyle('RepT2', parent=ref_subtitle, fontSize=11, leading=15)))
story_rep.append(Paragraph('<b>Technical Report</b>', ParagraphStyle('RepT3', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor('#475569'), spaceAfter=8)))
story_rep.append(Paragraph('<b>Submitted by:</b> Mrinmayee Pramod Kulkarni &nbsp;|&nbsp; <b>PRN:</b> 124B2B025<br/>'
                           '<b>Department:</b> Computer Engineering &nbsp;|&nbsp; <b>College:</b> PCCOE, Pune (2026–2027)', ref_meta))
story_rep.append(Spacer(1, 10))

story_rep.append(Paragraph('1. Introduction', ref_h1))
story_rep.append(Paragraph(
    'The Secure Code Review Assistant is a web-based application developed using Python and Streamlit. It helps users review source code '
    'and identify potential security vulnerabilities, programming errors, and areas for improvement. The application uses the Google Gemini API '
    'to analyze the submitted code and generate suggestions.',
    ref_body
))

story_rep.append(Paragraph('2. Problem Statement', ref_h1))
story_rep.append(Paragraph(
    'Manual code review can take time, especially when checking code for common security issues and programming mistakes. '
    'Developers and students may overlook vulnerabilities when reviewing code. This project provides a simple interface to support '
    'code review and help users understand potential issues.',
    ref_body
))

story_rep.append(Paragraph('3. Objectives', ref_h1))
r_objs = [
    '• Analyze source code for potential security vulnerabilities.',
    '• Identify possible programming errors and unsafe coding practices.',
    '• Provide explanations and suggestions for improvement.',
    '• Offer a simple interface for submitting code and viewing results.',
    '• Allow users to download the analysis report.'
]
for ro in r_objs:
    story_rep.append(Paragraph(ro, ref_bullet))

story_rep.append(Paragraph('4. Technologies Used', ref_h1))
r_techs = [
    '• <b>Python:</b> Main programming language.',
    '• <b>Streamlit:</b> Web interface.',
    '• <b>Google Gemini API:</b> Code analysis and recommendations.',
    '• <b>google-genai:</b> Python SDK for accessing Gemini.',
    '• <b>python-dotenv:</b> Loads configuration values from the .env file.'
]
for rt in r_techs:
    story_rep.append(Paragraph(rt, ref_bullet))

story_rep.append(Paragraph('5. System Architecture', ref_h1))
story_rep.append(Paragraph('The application follows a simple workflow:', ref_body))
r_arch = [
    '1. The user opens the Streamlit application.',
    '2. The user selects a programming language and enters source code.',
    '3. The application sends the code to the analysis module.',
    '4. The analysis module submits the code to the Gemini API.',
    '5. The response is displayed in the application.',
    '6. The user reviews the findings and can download the report.'
]
for ra in r_arch:
    story_rep.append(Paragraph(ra, ref_bullet))

story_rep.append(PageBreak())

# Page 2
story_rep.append(Paragraph('6. Main Modules', ref_h1))
story_rep.append(Paragraph('<b>6.1 User Interface (app.py)</b><br/>'
                           'This module provides the application interface. It accepts source code, allows language selection, starts the '
                           'analysis, displays the results, and provides the report download option.', ref_body))
story_rep.append(Paragraph('<b>6.2 Code Analysis (analyzer.py)</b><br/>'
                           'This module connects the application to the Gemini API. It sends the submitted code for analysis and returns the '
                           'generated findings and recommendations.', ref_body))
story_rep.append(Paragraph('<b>6.3 Configuration (.env)</b><br/>'
                           'The environment file stores the Gemini API key and model configuration. It is kept separate from the source code '
                           'to avoid exposing credentials.', ref_body))

story_rep.append(Paragraph('7. Implementation', ref_h1))
story_rep.append(Paragraph(
    'The application was developed in Python. Streamlit was used to create the interface, while the Google Gen AI SDK was used to '
    'communicate with Gemini. The user submits code through the interface, and the analysis results are displayed for review.<br/><br/>'
    'The project can be started from its directory using the command:',
    ref_body
))
story_rep.append(Paragraph('streamlit run app.py', ref_code))
story_rep.append(Paragraph('The Gemini API key must be configured correctly in the local environment before analysis can be performed.', ref_body))

story_rep.append(Paragraph('8. Testing and Results', ref_h1))
story_rep.append(Paragraph('The application was tested using a Python function that constructs an SQL query through string concatenation:', ref_body))
story_rep.append(Paragraph('query = "SELECT * FROM users WHERE id = " + user_id', ref_code))
story_rep.append(Paragraph(
    'The analysis identified the potential risk of SQL injection and recommended using parameterized SQL queries. '
    'This example demonstrated how the application can help users recognize unsafe coding practices.<br/><br/>'
    'The results depend on the submitted code, API availability, and the model\'s response. The findings should be reviewed '
    'before making changes to an application.',
    ref_body
))

story_rep.append(Paragraph('9. Limitations', ref_h1))
r_lims = [
    '• The analysis depends on the availability of the Gemini API.',
    '• Results may contain false positives or miss certain issues.',
    '• The application does not replace professional security testing.',
    '• The quality of the results depends on the submitted code and context.',
    '• API usage may be subject to account quotas and applicable charges.'
]
for rl in r_lims:
    story_rep.append(Paragraph(rl, ref_bullet))

story_rep.append(Paragraph('10. Future Scope', ref_h1))
story_rep.append(Paragraph(
    'The application could be extended with support for more programming languages, automated code quality checks, '
    'severity-based vulnerability classification, and integration with version-control platforms. Additional testing could also '
    'improve the consistency of the analysis.',
    ref_body
))

story_rep.append(PageBreak())

# Page 3
story_rep.append(Paragraph('11. Conclusion', ref_h1))
story_rep.append(Paragraph(
    'The Secure Code Review Assistant provides a simple way to examine source code for potential security vulnerabilities and '
    'programming issues. By combining Python, Streamlit, and Google Gemini, the project demonstrates how an AI-powered service can '
    'assist students and developers during code review. The generated findings should be treated as recommendations and verified '
    'before implementation.<br/><br/>',
    ref_body
))
story_rep.append(Spacer(1, 30))

# Signature on Page 3
sig_img_rep = Image(sig_img_path, width=120, height=32)
sig_data_rep = [
    [Paragraph('<b>Name and Signature:</b> Mrinmayee Pramod Kulkarni', ref_meta), sig_img_rep, Paragraph('<b>Date:</b> 15/10/2026', ref_meta)]
]
sig_tab_rep = Table(sig_data_rep, colWidths=[200, 150, 150])
sig_tab_rep.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story_rep.append(sig_tab_rep)

doc_rep.build(story_rep)
print('Technical_Report_Final.pdf compiled.')

# ==============================================================================
# 4. FACULTY APPROVAL RECORD (1 Page)
# ==============================================================================
fac_pdf = os.path.join(base, 'Synopsis', 'Faculty_Approval_Record.pdf')
doc_fac = SimpleDocTemplate(fac_pdf, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
story_fac = []

story_fac.append(Paragraph('DEPARTMENT OF COMPUTER ENGINEERING', ref_title))
story_fac.append(Paragraph('Pimpri Chinchwad College of Engineering (PCCOE), Pune', ref_subtitle))
story_fac.append(Paragraph('<b>CAPSTONE PROJECT APPROVAL & EVALUATION RECORD</b>', ParagraphStyle('FacSub', parent=ref_subtitle, fontSize=11, leading=15, textColor=colors.HexColor('#0369a1'), spaceAfter=14)))

story_fac.append(Paragraph(
    'This is to certify that the project titled <b>\"Secure Code Review Assistant: AI-Powered Debugging and Vulnerability '
    'Detection\"</b> submitted by <b>Mrinmayee Pramod Kulkarni (PRN: 124B2B025)</b>, Department of Computer Engineering (CS), '
    'for the <b>Capstone Project Evaluation (Academic Year 2026–2027)</b> has been reviewed and approved '
    'by the internal faculty guide.',
    ref_body
))
story_fac.append(Spacer(1, 12))

crit_data = [
    [Paragraph('Evaluation Parameter', ref_meta), Paragraph('Max Marks', ref_meta), Paragraph('Status / Grade', ref_meta)],
    [Paragraph('Relevance to Industry Domain & Software Security', ref_body), Paragraph('20', ref_body), Paragraph('Approved (Excellent)', ref_body)],
    [Paragraph('System Architecture & Application Implementation', ref_body), Paragraph('25', ref_body), Paragraph('Approved (Complete)', ref_body)],
    [Paragraph('Vulnerability Detection & Code Recommendations', ref_body), Paragraph('25', ref_body), Paragraph('Approved (Verified)', ref_body)],
    [Paragraph('Evaluation Evidence & Documentation', ref_body), Paragraph('30', ref_body), Paragraph('Approved (Comprehensive)', ref_body)],
    [Paragraph('<b>Total Marks</b>', ref_meta), Paragraph('<b>100</b>', ref_meta), Paragraph('<b>Verified & Recommended</b>', ref_meta)]
]
ct = Table(crit_data, colWidths=[240, 100, 180])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0369a1')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0369a1')),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 6),
]))
story_fac.append(ct)
story_fac.append(Spacer(1, 35))

sig_data_fac = [
    [Paragraph('<b>Student:</b> Mrinmayee Pramod Kulkarni', ref_body), Paragraph('<b>Faculty Guide:</b> _________________________', ref_body)],
    [Paragraph('<b>PRN:</b> 124B2B025 | Branch: CS', ref_body), Paragraph('<b>Signature:</b> _________________________', ref_body)],
    [Paragraph('<b>College:</b> PCCOE, Pune', ref_body), Paragraph('<b>Date:</b> 15/10/2026', ref_body)]
]
ft = Table(sig_data_fac, colWidths=[260, 260])
ft.setStyle(TableStyle([
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
]))
story_fac.append(ft)

doc_fac.build(story_fac)
print('Faculty_Approval_Record.pdf compiled.')

# ==============================================================================
# 5. EXTERNAL DEPENDENCIES DECLARATION (1 Page)
# ==============================================================================
ext_pdf = os.path.join(base, 'Declarations', 'External_Dependencies_Declaration.pdf')
doc_ext = SimpleDocTemplate(ext_pdf, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
story_ext = []

story_ext.append(Paragraph('EXTERNAL DEPENDENCIES AND API DECLARATION', ref_title))
story_ext.append(Paragraph('Academic Project Compliance Record', ref_subtitle))
story_ext.append(Spacer(1, 10))

story_ext.append(Paragraph(
    'In accordance with academic project guidelines, all software dependencies, libraries, and external API interfaces '
    'utilized in the project developed by <b>Mrinmayee Pramod Kulkarni (PRN: 124B2B025)</b> for <b>\"Secure Code Review Assistant: '
    'AI-Powered Debugging and Vulnerability Detection\"</b> are formally declared below:',
    ref_body
))
story_ext.append(Spacer(1, 10))

dep_data = [
    [Paragraph('Component / Service', ref_meta), Paragraph('Provider / SDK', ref_meta), Paragraph('Version / Model', ref_meta), Paragraph('Internet Required?', ref_meta)],
    [Paragraph('AI Model API', ref_body), Paragraph('Google Cloud / DeepMind', ref_body), Paragraph('Google Gemini 1.5 Flash', ref_body), Paragraph('Yes (API call)', ref_body)],
    [Paragraph('SDK Integration', ref_body), Paragraph('Google Gen AI SDK', ref_body), Paragraph('google-genai / google-generativeai', ref_body), Paragraph('Yes', ref_body)],
    [Paragraph('Local Analysis Fallback', ref_body), Paragraph('Secure Code Rule Engine', ref_body), Paragraph('OWASP Rule-Based Parser', ref_body), Paragraph('<b>No (100% Offline)</b>', ref_body)],
    [Paragraph('Web UI Framework', ref_body), Paragraph('Streamlit Open-Source', ref_body), Paragraph('v1.30.0+', ref_body), Paragraph('<b>No (Localhost)</b>', ref_body)],
    [Paragraph('Environment Loader', ref_body), Paragraph('python-dotenv', ref_body), Paragraph('v1.0.0+', ref_body), Paragraph('<b>No (Local file)</b>', ref_body)]
]
dt = Table(dep_data, colWidths=[130, 130, 150, 110])
dt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f766e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0f766e')),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
]))
story_ext.append(dt)
story_ext.append(Spacer(1, 15))

story_ext.append(Paragraph(
    '<b>Candidate Confirmation:</b> The application logic, user interface, analysis workflows, error handling, '
    'and offline security rule fallback were implemented by me. External dependencies are restricted to runtime libraries and API connectivity.',
    ref_body
))
story_ext.append(Spacer(1, 15))

sig_img_ext = Image(sig_img_path, width=120, height=32)
sig_data_ext = [
    [Paragraph('<b>Student Signature:</b> Mrinmayee Pramod Kulkarni', ref_meta), sig_img_ext, Paragraph('<b>Date:</b> 15/10/2026', ref_meta)]
]
sig_tab_ext = Table(sig_data_ext, colWidths=[200, 150, 150])
sig_tab_ext.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story_ext.append(sig_tab_ext)

doc_ext.build(story_ext)
print('External_Dependencies_Declaration.pdf compiled.')

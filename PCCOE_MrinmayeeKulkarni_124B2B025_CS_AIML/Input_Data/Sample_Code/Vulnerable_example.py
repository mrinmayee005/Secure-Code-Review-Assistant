# Input_Data/Sample_Code/Vulnerable_example.py
# Demonstration code containing CWE-89 SQL Injection flaw
# Academic Year: 2026-2027 | PCCOE Pune

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return execute_query(query)

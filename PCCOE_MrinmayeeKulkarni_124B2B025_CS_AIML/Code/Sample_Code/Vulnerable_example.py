# Sample_Code/Vulnerable_example.py
# Reference test input containing SQL Injection vulnerability (CWE-89)
# Used for demonstrating AI-Powered Debugging and Vulnerability Detection

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return execute_query(query)

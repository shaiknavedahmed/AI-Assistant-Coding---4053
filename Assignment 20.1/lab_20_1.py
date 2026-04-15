'''Task 1 – Input Validation Check
Task:
Analyze an AI-generated Python login script for input validation
vulnerabilities.
Instructions:
• Prompt AI to generate a simple username-password
login program.
• Review whether input sanitization and validation are
implemented.
• Suggest secure improvements (e.g., using re for input
validation).
Expected Output:
• A secure version of the login script with proper input
validation.'''

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# Improved version with input validation
import re
import getpass

def validate_username(username):
    # Only letters and numbers, 3–15 characters
    return re.fullmatch(r"[A-Za-z0-9]{3,15}", username)

def validate_password(password):
    # At least 6 chars, 1 letter + 1 number
    return re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}", password)

def login():
    username = input("Enter username: ").strip()
    
    if not validate_username(username):
        print("Invalid username format!")
        return

    password = getpass.getpass("Enter password: ")

    if not validate_password(password):
        print("Invalid password format!")
        return

    # Dummy stored credentials
    if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")

login()

#Task 2
'''Task 2 – SQL Injection Prevention
Task:
Test an AI-generated script that performs SQL queries on a
database.
Instructions:
• Ask AI to generate a Python script using SQLite/MySQL to
fetch user details.
• Identify if the code is vulnerable to SQL injection (e.g.,
using string concatenation in queries).
• Refactor using parameterized queries (prepared
statements).
Expected Output:
• A secure database query script resistant to SQL
injection.'''

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")

#  Vulnerable to SQL Injection
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)

conn.close()

#Task 4
import requests

username = input("Enter username: ")
password = input("Enter password: ")

# ❌ Hardcoded API URL with user input directly
url = f"https://api.example.com/login?user={username}&pass={password}"

response = requests.get(url)

if response.status_code == 200:
    print("Login Success:", response.text)
else:
    print("Login Failed")

#give a secure version of the above code using parameterized requests
import requests
import re
import getpass

def validate_username(username):
    return re.fullmatch(r"[A-Za-z0-9]{3,15}", username)

def validate_password(password):
    return len(password) >= 6

def login():
    username = input("Enter username: ").strip()
    
    if not validate_username(username):
        print("Invalid username format")
        return

    password = getpass.getpass("Enter password: ")

    if not validate_password(password):
        print("Password too short")
        return

    url = "https://api.example.com/login"

    try:
        # ✅ Use POST instead of GET
        response = requests.post(
            url,
            json={"username": username, "password": password},
            timeout=5
        )

        response.raise_for_status()

        print("Login Success:", response.json())

    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

login()

#Task 5
'''Task 5 – Insecure Data Serialization Check
Task:
Evaluate AI-generated code that uses pickle for saving user
data.
Instructions:
• Ask AI to generate a script using pickle.load().
• Explain why untrusted pickle data is dangerous.
• Replace with safer formats like JSON.
Expected Output:
• Secure serialization code using JSON instead of pickle.'''

import pickle

# Save user data
data = {"username": "naved", "score": 95}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load user data
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)   # ❌ Dangerous

print(loaded_data)

# Secure version using JSON
import json

# Save user data
data = {"username": "naved", "score": 95}

with open("data.json", "w") as f:
    json.dump(data, f)

# Load user data
with open("data.json", "r") as f:
    loaded_data = json.load(f)   # ✅ Safe

print(loaded_data)
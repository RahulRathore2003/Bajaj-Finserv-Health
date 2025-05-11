# Bajaj-Finserv-Health
import requests

# Step 1: Generate webhook
generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
payload = {
    "name": "Rahul Rathore", 
    "regNo": "0827AL221106",  # your actual regNo here 
    "email": "rahulrathoreacro2003@gmail.com" 
}

response = requests.post(generate_url, json=payload)
data = response.json()

# Extract webhook and token
webhook_url = data['webhook']
access_token = data['accessToken']

# Final SQL query
final_query = """
SELECT 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE e1
JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN EMPLOYEE e2 
    ON e1.DEPARTMENT = e2.DEPARTMENT
    AND e1.DOB < e2.DOB
GROUP BY 
    e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
ORDER BY 
    e1.EMP_ID DESC;
"""

# Step 2: Submit final SQL query
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}
submit_payload = {
    "finalQuery": final_query
}

submit_response = requests.post(webhook_url, json=submit_payload, headers=headers)

print("Submitted:", submit_response.status_code)
print("Response:", submit_response.text)



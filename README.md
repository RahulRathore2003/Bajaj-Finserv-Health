# 🩺 Bajaj Finserv Health – Qualifier 1 (Python)

## 👤 Candidate Information

- **Name**: Rahul Rathore  
- **Reg No**: 0827AL221106  
- **Email**: rahulrathoreacro2003@gmail.com  

---

## 🚀 Problem Statement

Build a Python application that:

1. Sends a `POST` request to generate a **webhook and token**.
2. Based on the returned SQL problem, submits the **final SQL query**.
3. Uses the webhook and token for **secure submission**.

Your task was determined based on the last digit of the regNo (even number → **Question 2**).

## 🧠 SQL Problem Summary
You are required to calculate the number of employees who are younger than each 
employee, grouped by their respective departments. For each employee, return the 
count of employees in the same department whose age is less than theirs.
Output Format:
• The output should contain the following columns:
1. EMP_ID: The ID of the employee.
2. FIRST_NAME: The first name of the employee.
3. LAST_NAME: The last name of the employee.
4. DEPARTMENT_NAME: The name of the department the employee 
belongs to.
5. YOUNGER_EMPLOYEES_COUNT: The number of employees who are 
younger than the respective employee in their department.
The output should be ordered by employee ID in descending orde

## 🧾 Final SQL Query

```sql
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

## How to Run the Code
pip install requests
python main.py



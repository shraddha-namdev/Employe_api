# Employe_api# Employee Management API (Flask + SQLAlchemy)

A simple RESTful API built with Flask and SQLAlchemy to manage employees.

## Features
- Add new employee
- Get all employees
- Get employee by ID
- Update employee details
- Delete employee

## Tech Stack
- Python, Flask
- SQLite, SQLAlchemy
- Postman for testing

## Run Locally
```bash
pip install -r requirements.txt
python app.py


**##How to Test**
Run the app → python app.py

Use Postman:

POST /employees → Add new employee

GET /employees → Get all employees

GET /employees/1 → Get employee by ID

PUT /employees/1 → Update employee

DELETE /employees/1 → Delete employee

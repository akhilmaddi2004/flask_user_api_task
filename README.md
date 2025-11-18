### Flask REST API – User Management

This project is the solution for Task 4 of the Python Developer Internship at Elevate Labs.
The goal was to build a simple REST API using Flask that can manage user data.

The API supports the following operations:

- Create a user
- Read all users
- Read a user by ID
- Update a user
- Delete a user

Everything is stored in in-memory data during runtime.

## 1. Project Structure

/task4-flask-api
│
├── app.py
├── requirements.txt

## 2. How the API Works

The API uses a Python dictionary called users_db to store data while the server is running.
Each user has:

- id
- name
- email
- age

The application exposes REST routes to interact with this data.

## 3. Installation and Setup

# Step 1: Install dependencies

- pip install -r requirements.txt

# Step 2: Run the Flask app

- python app.py

- The server will start at:

- http://127.0.0.1:5000/

## 4. API Endpoints and Testing

You can test this API using:
- Browser (GET requests)
- CMD curl commands (POST, PUT, DELETE)
Below are all required tests.

# A) Create a User (POST)

curl -X POST http://127.0.0.1:5000/users ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Akhil\", \"email\":\"akhil@test.com\", \"age\":22}"

Response:

{
  "id": 1,
  "name": "Akhil",
  "email": "akhil@test.com",
  "age": 22
}

# B) Get All Users (GET)

- Open in browser:

http://127.0.0.1:5000/users

# C) Get User by ID (GET)

- Open in browser:

http://127.0.0.1:5000/users/1

# D) Update User (PUT)

curl -X PUT http://127.0.0.1:5000/users/1 ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Akhil Updated\"}"

## E) Delete User (DELETE)

curl -X DELETE http://127.0.0.1:5000/users/1

5. Key Concepts Used

- Flask framework
- REST architecture
- HTTP methods (GET, POST, PUT, DELETE)
- Routing and request handling
- JSON responses
- In-memory data storage

## 6. Outcome

This task builds a clear understanding of:

- How REST APIs work
- How Flask routes process requests
- How to send data using JSON
- How CRUD operations work in backend development

This is a core skill for any Python backend developer.

---

If you want, I can rewrite it shorter, more stylish, or more professional.

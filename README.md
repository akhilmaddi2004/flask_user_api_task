## 🚀 Flask REST API – User Management

Task 4 – Python Developer Internship (Elevate Labs)

This project is a REST API built using Flask.
It manages user data using in-memory storage and supports all essential CRUD operations.

The goal of this task was to understand:

- 🔹 REST concepts
- 🔹 HTTP methods
- 🔹 Flask routing
- 🔹 JSON handling
- 🔹 API testing using browser + curl

## 📁 Project Structure

- /task4-flask-api
- │
- ├── app.py               # Main Flask application
- ├── requirements.txt     # Dependencies

The project is intentionally simple because the task requires API fundamentals, not databases.

## 📌 Features Implemented

- ✔ Create a user
- ✔ Fetch all users
- ✔ Fetch a user by ID
- ✔ Update a user
- ✔ Delete a user
- ✔ JSON responses
- ✔ Error handling for invalid IDs

All operations are handled using a dictionary (users_db) that acts as temporary storage.

## 🛠 Installation & Setup

1️⃣ Install dependencies

- pip install -r requirements.txt

2️⃣ Run the Flask server

- python app.py

3️⃣ API Base URL

- http://127.0.0.1:5000/

## 📡 API Endpoints & Testing Guide

Below are all required API tests, exactly matching the task instructions.

🟦 1. Create User (POST)

- Use CMD:

curl -X POST http://127.0.0.1:5000/users ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Akhil\", 
\"email\":\"akhil@test.com\", \"age\":22}"

- ✔ Expected Response:

{
  "id": 1,
  "name": "Akhil",
  "email": "akhil@test.com",
  "age": 22
}


🟩 2. Get All Users (GET)

- Open in your browser:

- http://127.0.0.1:5000/users

🟨 3. Get User by ID (GET)

- http://127.0.0.1:5000/users/1

🟧 4. Update User (PUT)

curl -X PUT http://127.0.0.1:5000/users/1 ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Akhil Updated\"}"

🟥 5. Delete User (DELETE)

curl -X DELETE http://127.0.0.1:5000/users/1

## 🧠 Key Concepts Learned

-- 🔹 REST Architecture
- Stateless communication
- Resource-based endpoints

-- 🔹 HTTP Methods
- GET → Retrieve
- POST → Create
- PUT → Update
- DELETE → Remove

-- 🔹 Flask Concepts
- Routing with decorators
- JSON request handling (request.json)
- Returning JSON responses with proper status codes

-- 🔹 API Testing
- Browser for GET
- curl commands for POST, PUT, DELETE

## 🎯 Outcome

This task builds a solid foundation in:
- Backend development
- API creation
- Data handling
- Practical Flask usage
- CLI-based API testing

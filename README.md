# Flask User Management API

A **RESTful Flask API** for managing user data — allowing you to **create, read, update, and delete** users.  
Built with:

- ⚙️ **Flask** — Python micro web framework  
- 🧱 **SQLAlchemy** — ORM for database handling  
- 🧮 **Marshmallow** — Data serialization/deserialization  
- 💾 **SQLite** — Lightweight, file-based database  

---

## 🚀 Features

- ✅ Add new users  
- ✅ Get all users or a single user by ID  
- ✅ Update user information  
- ✅ Delete a user  
- ✅ JSON-based communication  
- ✅ Easily testable with **Postman** or `curl`

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/nehanasir987/flask_-api.git
cd flask_-api

###2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

###3. Install dependencies
pip install -r requirements.txt
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy


###4. Run the application
python app.py

🧪 API Endpoints & Examples (Postman / curl)
⚠️ Important: Make sure the app is running and set this header in Postman:
Content-Type: application/json

🟢 1️⃣ Create User — POST
POST http://127.0.0.1:5000/user
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "12345"
}
Request Body (JSON)
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "12345"
}

<img width="1366" height="768" alt="POST Method" src="https://github.com/user-attachments/assets/f8ccc2ed-aa16-4d64-b3e4-6249311151b0" />

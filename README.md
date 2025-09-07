---

# 📝 To-Do App with Database

A simple but professional **To-Do API** built with **FastAPI**, **SQLAlchemy ORM**, and **Alembic** migrations.
Supports **SQLite** (default) and **PostgreSQL**, with secure JWT authentication.

---

## 🚀 Features

* 🔐 **User Authentication** (Register/Login with hashed passwords & JWT tokens)
* ✅ **CRUD Operations** for tasks (create, list, update, delete)
* 👤 **User → Task Relationship** (tasks belong to users)
* 🗄 **SQLAlchemy ORM** for database models
* 🔄 **Alembic** for database migrations
* 📖 Interactive API docs (Swagger & ReDoc via FastAPI)

---

## 🏗 Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** SQLite (dev) / PostgreSQL (prod)
* **ORM:** SQLAlchemy 2.0
* **Migrations:** Alembic
* **Auth:** OAuth2 + JWT (using `python-jose` and `passlib`)
* **Containerization (optional):** Docker

---

## 📂 Project Structure

```
todo-app/
├─ app/
│  ├─ main.py             # FastAPI entrypoint
│  ├─ core/config.py      # App settings
│  ├─ db/                 # DB engine & session
│  ├─ models/             # SQLAlchemy models
│  ├─ schemas/            # Pydantic schemas
│  ├─ crud/               # CRUD operations
│  ├─ api/                # Routers (users & tasks)
│  └─ security.py         # Hashing & JWT utils
├─ alembic/               # Migrations
├─ requirements.txt
├─ alembic.ini
├─ Dockerfile
└─ README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file:

```
DATABASE_URL=sqlite:///./todo.db
SECRET_KEY=replace_with_random_secret
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

For PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost:5432/tododb
```

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the app

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Endpoints

### Auth

* `POST /api/users/` → Register new user
* `POST /api/users/token` → Login & get JWT token

### Tasks (requires Bearer token)

* `POST /api/tasks/` → Create task
* `GET /api/tasks/` → List user tasks
* `GET /api/tasks/{id}` → Get specific task
* `PUT /api/tasks/{id}` → Update task
* `DELETE /api/tasks/{id}` → Delete task

---

## 🔑 Example Usage

Register:

```bash
curl -X POST "http://127.0.0.1:8000/api/users/" \
-H "Content-Type: application/json" \
-d '{"email":"alice@example.com","password":"secret"}'
```

Login:

```bash
curl -X POST "http://127.0.0.1:8000/api/users/token" \
-F "username=alice@example.com" \
-F "password=secret"
```

Create Task:

```bash
curl -X POST "http://127.0.0.1:8000/api/tasks/" \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk","description":"2 liters"}'
```

---

## 🐳 Run with Docker (Optional)

```bash
docker build -t todo-app .
docker run -d -p 8000:80 --env-file .env todo-app
```

---

## 🛠 Future Improvements

* 🔄 Refresh tokens & logout
* 📧 Email verification & password reset
* 🧪 Unit & integration tests with Pytest
* 📊 Admin dashboard
* 🌐 Frontend (React/Next.js)

---

## 📜 License

This project is licensed under the MIT License.

---

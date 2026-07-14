# 🤖 Real-Time AI Chat API (MVP)

A modern, production-style Real-Time AI Chat Backend built with **FastAPI**, **WebSocket**, **Google Gemini AI**, and **SQLite**.

This project is designed as a **Minimum Viable Product (MVP)** to demonstrate a clean backend architecture for a real-time AI-powered chat application. It focuses on authentication, persistent chat history, WebSocket communication, and AI integration while keeping the codebase simple, scalable, and easy to extend.

---

# ✨ Features

- 🔐 User Signup & Login
- 🔑 JWT Authentication
- ⚡ Real-Time Chat using WebSocket
- 🤖 Google Gemini AI Integration
- 💬 AI-generated Responses
- 📝 Persistent Chat History
- 👤 Multiple User Support
- 🗄️ SQLite Database
- 📦 SQLAlchemy ORM
- ✅ Pydantic Request & Response Validation
- ⚙️ Environment-based Configuration
- 🧩 Modular Project Structure
- 🚀 Deployment Ready Backend
- 📚 Clean and Maintainable Code

---

# 🛠 Tech Stack

- Python
- FastAPI
- WebSocket
- Google Gemini API
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Passlib (Bcrypt)
- Uvicorn

---

# 📁 Project Structure

```text
app/
│
├── main.py
├── config.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── crud.py
├── ai_service.py
├── websocket.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file.

```env
DATABASE_URL=sqlite:///./chat.db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Installation

```bash
git clone <repository_url>

cd project

pip install -r requirements.txt

uvicorn main:app --reload
```

---

# 🔗 API Endpoints

## Authentication

```
POST /signup

POST /login
```

## WebSocket

```
/ws/chat/{chat_id}
```

---

# 💬 Chat Flow

```text
User

↓

WebSocket

↓

FastAPI

↓

Gemini AI

↓

AI Response

↓

WebSocket

↓

User
```

---

# 🗄 Database Tables

### Users

- id
- username
- email
- hashed_password
- is_active
- created_at

### Chats

- id
- user_id
- title
- created_at

### Messages

- id
- chat_id
- role
- content
- created_at

---

# 🔒 Authentication

JWT (JSON Web Token) is used for secure authentication.

Passwords are securely hashed using **Bcrypt** before being stored in the database.

---

# 🚀 Deployment

This backend can be deployed on platforms such as:

- Render
- Railway
- VPS
- Docker (Future)

---

# 📌 Future Improvements

The following features are **planned for future versions** and are **not included in this MVP**:

- PostgreSQL Support
- Redis Caching
- Refresh Token Authentication
- Role-Based Access Control (RBAC)
- Streaming AI Responses
- Conversation Memory
- RAG (Retrieval-Augmented Generation)
- PDF & Document Chat
- File Upload Support
- Image Generation
- Voice Chat
- Multi-Agent AI
- AI Conversation Titles
- Rate Limiting
- Logging & Monitoring
- Docker Support
- CI/CD Pipeline
- Unit & Integration Tests

---

# 🎯 Project Goal

This project demonstrates how to build a clean, scalable, and production-style backend for a Real-Time AI Chat application using modern Python technologies while keeping the MVP focused on core functionality.

---

# 📄 License

This project is released under the MIT License.

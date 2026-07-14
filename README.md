# 🤖 Real-Time AI Chat API (MVP)

A modern, production-style Real-Time AI Chat Backend built with FastAPI, WebSocket, Google Gemini AI, and SQLite.

This project is designed as a Minimum Viable Product (MVP) to demonstrate a clean backend architecture for a real-time AI-powered chat application. It focuses on authentication, persistent chat history, WebSocket communication, and AI integration while keeping the codebase simple, scalable, and easy to extend.

---

# ✨ Features

- 🔐 User Signup & Login
- 🔑 JWT Authentication
- 🛡️ JWT Token Verification Dependency
- ⚡ Real-Time Chat using WebSocket
- 🤖 Google Gemini AI Integration
- 💬 AI-generated Responses
- 📝 Persistent Chat History
- 👤 Multiple User Support
- 🛣️ Dedicated Chat API Routes
- ⚠️ Global Exception & Error Handling
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
├── dependencies.py
├── chat_routes.py
├── exceptions.py
├── requirements.txt
└── README.md

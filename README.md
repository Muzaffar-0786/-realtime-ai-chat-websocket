# 🚀 Real-Time AI Chat Backend

A modern Real-Time AI Chat Backend built with FastAPI, WebSocket, SQLAlchemy, JWT Authentication, and Google Gemini AI.

This project is developed as a Minimum Viable Product (MVP) that demonstrates a complete AI-powered chat workflow.

Users can register, login securely, create chats, send messages in real-time using WebSocket, receive AI-generated responses from Google Gemini, and store conversation history.

The project follows a clean and modular backend architecture designed for easy maintenance, extension, and deployment.

---

# ✨ Features

## Authentication

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Protected API Access

## AI Chat System

- Google Gemini AI Integration
- Real-Time Chat using WebSocket
- AI Response Generation
- Conversation History Support
- AI Response Validation
- Safe Fallback Response
- Error Handling

## Chat Management

- Create Chat
- Retrieve Chat
- Store User Messages
- Store AI Messages
- Fetch Previous Conversation History

## Backend Features

- FastAPI Framework
- SQLAlchemy ORM
- SQLite Database
- Pydantic Validation
- REST API Support
- WebSocket Communication
- Swagger API Documentation
- Environment Variable Support

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Database

- SQLite

## Authentication

- JWT Authentication
- Password Hashing

## AI

- Google Gemini AI
- google-generativeai SDK

## Communication

- REST API
- WebSocket

---

# 📂 Project Structure

real-time-ai-chat/

├── main.py  
├── database.py  
├── models.py  
├── schemas.py  
├── crud.py  
├── auth.py  
├── ai_service.py  
├── websocket.py  

├── requirements.txt  
├── README.md  
├── .gitignore  
├── .env  

---

# ⚙️ Installation

## Clone Repository

git clone <repository-url>

## Install Dependencies

pip install -r requirements.txt

## Environment Setup

Create a `.env` file and add:

GEMINI_API_KEY=your_gemini_api_key

SECRET_KEY=your_secret_key

Keep environment variables private and never upload them to GitHub.
# ▶️ Running The Application

Start the FastAPI server:

uvicorn main:app --reload

The application will start on:

http://127.0.0.1:8000


---

# 📖 API Documentation

FastAPI provides automatic interactive documentation.

Open:

/docs

Example:

http://127.0.0.1:8000/docs

Using Swagger UI, you can test available API endpoints.


---

# 🔌 WebSocket Chat Flow

The application uses WebSocket for real-time communication between client and server.

Flow:

User Message

↓

WebSocket Connection

↓

Validate Request

↓

Save User Message

↓

Fetch Chat History

↓

Send Context To Gemini AI

↓

Generate AI Response

↓

Save AI Response

↓

Send Response Back To User


---

# 🤖 AI Integration Flow

Google Gemini AI is connected through the AI service layer.

Current AI workflow:

- Receive user message
- Load previous conversation history
- Send request to Gemini AI
- Generate response
- Validate response
- Return safe fallback if AI service fails


---

# 🗄 Database Management

The application stores:

- User Data
- Chat Data
- User Messages
- AI Messages
- Conversation History

SQLAlchemy ORM is used for database operations.


---

# 🔐 Security

Current security implementation:

- JWT Authentication
- Password Hashing
- Environment Variable Support
- Input Validation

Important:

Never expose API keys or secret keys publicly.


---

# 📌 Current MVP Status

Completed Features:

✅ User Authentication  
✅ JWT Login System  
✅ Chat Management  
✅ Real-Time WebSocket Chat  
✅ Google Gemini AI Integration  
✅ Conversation History  
✅ Database Storage  
✅ Error Handling  


---

# 🚧 Future Improvements

The following features can be added in future versions:

## AI Improvements

- Streaming AI Responses
- Better AI Context Management
- Multiple AI Model Support

## Chat Improvements

- Chat Search
- Chat Rename
- Chat Delete Improvements
- File Upload Support
- Image AI Support
- Voice Chat

## Backend Improvements

- PostgreSQL Support
- Redis Cache
- Docker Deployment
- Automated Testing
- CI/CD Pipeline
- Advanced Monitoring


---

# 🚀 Deployment

For deployment:

1. Install dependencies

pip install -r requirements.txt


2. Add environment variables


3. Start FastAPI server

uvicorn main:app --host 0.0.0.0 --port 8000


The project can be deployed on platforms supporting Python applications.


---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Commit changes.
5. Create a Pull Request.


---

# 📄 License

This project is licensed under the MIT License.


---

# ⭐ Project Summary

Real-Time AI Chat Backend is an MVP project that combines:

- FastAPI Backend
- Real-Time WebSocket Communication
- Gemini AI Integration
- Database Management
- Secure Authentication

The architecture is designed to allow future improvements and scaling.

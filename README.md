# 🤖 TaskAI - AI Powered Knowledge Assistant

## 📌 Overview

TaskAI is a full-stack AI-powered application that allows users to upload documents and ask questions based on their content.

The system uses a simple Retrieval-Augmented Generation (RAG) approach:

* Upload document → split into chunks
* Ask question → use chunks as context
* Generate answer using OpenAI

---

## 🚀 Features

* 📄 Upload text documents
* ✂️ Automatic text chunking
* ❓ Ask questions from document context
* 🤖 AI-generated answers
* ⚡ Fast and simple UI

---

## 🛠 Tech Stack

* **Frontend:** React.js
* **Backend:** Django + Django REST Framework
* **AI:** OpenAI API
* **Database:** SQLite

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Muskangupta2909/TaskAI.git
cd TaskAI
```

---

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

👉 Create `.env` file inside `backend/` and add:

```env
OPENAI_API_KEY=your_api_key_here
```

```bash
python manage.py migrate
python manage.py runserver
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 📡 API Endpoints

### Upload Document

```
POST /upload-doc/
```

### Ask Question

```
POST /ask/
```

---

## 🧠 How It Works

1. User uploads a document
2. Backend reads and splits it into chunks
3. When a question is asked:

   * Relevant chunks are selected
   * Sent as context to OpenAI API
4. AI generates answer based only on context

---

## ⚠️ Important Notes

* `.env` file is required for API key
* Do NOT expose your API key publicly
* Works best with `.txt` files

---

## 👩‍💻 Author

Muskan Gupta

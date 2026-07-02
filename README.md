# SHL Assessment Recommendation System

An AI-powered recommendation system that helps recruiters identify the most suitable SHL assessments based on hiring requirements. The system uses Retrieval-Augmented Generation (RAG) with semantic search over the SHL product catalog and Gemini for intelligent recommendations.

---

## Features

- AI-powered assessment recommendations
- Semantic search using Sentence Transformers
- FAISS vector database for fast retrieval
- Google Gemini integration
- Context-aware conversation handling
- Assessment comparison
- Clarification questions for incomplete queries
- Protection against prompt injection
- Off-topic query rejection
- FastAPI REST API
- Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Google Gemini
- Pydantic
- NumPy

---

## Project Architecture

```
User Query
      │
      ▼
FastAPI
      │
      ▼
SHL Agent
      │
      ▼
Retriever (FAISS)
      │
      ▼
Top Matching Assessments
      │
      ▼
Gemini
      │
      ▼
Structured JSON Response
```

---

## Project Structure

```
SHL_Assessment_Recommender/

│── app/
│   ├── agent.py
│   ├── catalog.py
│   ├── llm.py
│   ├── main.py
│   ├── models.py
│   ├── prompts.py
│   └── retriever.py
│
│── data/
│   └── shl_catalog.json
│
│── vector_db/
│   └── shl_index.faiss
│
│── .env
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone <your-github-repository>
```

Go to project

```bash
cd SHL_Assessment_Recommender
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the API

```bash
python -m uvicorn app.main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET /

Returns API status.

---

### GET /health

Health check endpoint.

---

### POST /chat

Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I am hiring a Java Developer with 3 years of experience."
    }
  ]
}
```

Example Response

```json
{
  "reply": "Based on the retrieved SHL catalog, these assessments are recommended.",

  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "...",
      "test_type": "Knowledge"
    }
  ],

  "end_of_conversation": true
}
```

---

## Intelligent Behaviors

The system supports:

- Assessment recommendation
- Assessment comparison
- Multi-turn conversation
- Clarification questions
- Prompt injection protection
- Off-topic query rejection

---

## Retrieval Pipeline

1. User query
2. Convert query into embedding
3. Search FAISS vector database
4. Retrieve top matching SHL assessments
5. Send retrieved context to Gemini
6. Generate structured JSON response

---

## Future Improvements

- Hybrid Search (BM25 + Semantic Search)
- Conversation Memory
- Assessment Ranking Model
- Docker Deployment
- Multi-language Support

---

## Author

Ayushi Saxena

B.Tech Computer Science Engineering

KIET Group of Institutions

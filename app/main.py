from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agent import SHLAgent
from app.models import ChatRequest

app = FastAPI(
    title="SHL Assessment Recommendation API",
    version="1.0.0"
)

# -----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------

agent = SHLAgent()

# -----------------------------------------------------

@app.get("/")

def home():

    return {
        "message": "SHL Assessment Recommendation API is running."
    }

# -----------------------------------------------------

@app.get("/health")

def health():

    return {
        "status": "ok"
    }

# -----------------------------------------------------

@app.post("/chat")

def chat(request: ChatRequest):

    messages = []

    for message in request.messages:

        messages.append(
            {
                "role": message.role,
                "content": message.content
            }
        )

    response = agent.chat(messages)

    return response

# -----------------------------------------------------
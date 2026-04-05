from fastapi import FastAPI

from app.api import chat, news, events, feedback, management, grants
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()

app.include_router(chat.router)
app.include_router(news.router)
app.include_router(events.router)
app.include_router(feedback.router)
app.include_router(management.router)
app.include_router(grants.router)


@app.get("/")
def root():
    return {"message": "API ishlayapti 🔥"}

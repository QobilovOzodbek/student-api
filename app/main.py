from fastapi import FastAPI

from app.api import chat, news, events, feedback

app = FastAPI(title="Student Chatbot API 🚀")

app.include_router(chat.router)
app.include_router(news.router)
app.include_router(events.router)
app.include_router(feedback.router)


@app.get("/")
def root():
    return {"message": "API ishlayapti 🔥"}
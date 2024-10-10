from fastapi import FastAPI, Request
from pydantic import BaseModel
from database import get_restaurants, get_restaurant_by_name, update_database
from spider import run_spider
import nltk
from nltk.chat.util import Chat, reflections

app = FastAPI()

pairs = [
    ['hi', ['Hello! How can I help you?']],
    ['what is your name?', ['My name is Chatbot!']],
    ['show me restaurants', ['Here are some restaurants: %s' % get_restaurants()]],
    ['tell me about (.*)', ['Here is what I found: %s' % get_restaurant_by_name('%1')]],
    # Add more pairs of questions and answers here
]

def chatbot_response(message):
    chat = Chat(pairs, reflections)
    return chat.respond(message)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chatbot API"}

@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.message
    response = chatbot_response(user_input)
    return {"response": response}

@app.post("/scrape")
async def scrape():
    run_spider()
    update_database('data/restaurants.json')
    return {"status": "Scraping and database update started"}

if __name__ == "__main__":
    nltk.download('punkt')
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
# app.py
from flask import Flask, request, jsonify
from nlp_chatbot import chatbot

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot_response(user_input)
    return jsonify({'response': response})

def chatbot_response(message):
    # Aqui você pode integrar a lógica do chatbot
    return "Esta é uma resposta do chatbot."

if __name__ == "__main__":
    app.run(debug=True)
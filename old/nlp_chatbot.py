# nlp_chatbot.py
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['oi', ['Olá! Como posso ajudar?']],
    ['qual o seu nome?', ['Meu nome é Chatbot!']],
    # Adicione mais pares de perguntas e respostas aqui
]

def chatbot():
    print("Olá! Eu sou um chatbot. Como posso ajudar?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
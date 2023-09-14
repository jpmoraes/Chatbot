from flask import Flask, request, jsonify
import random
import nltk

nltk.download('punkt')

# Pares de perguntas e respostas
perguntas_respostas = {
    "Olá": "Olá! Como posso ajudar você?",
    "Como você está?": "Estou bem, obrigado por perguntar.",
    "Qual é o seu nome?": "Meu nome é ChatBot.",
    "O que você pode fazer?": "Posso responder a perguntas simples.",
    "Tchau": "Tchau! Tenha um bom dia!"
}



app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_question = data['question']
    resposta = responder_pergunta(user_question)
    return jsonify({'response': resposta})

def responder_pergunta(pergunta):
    resposta = perguntas_respostas.get(pergunta)
    if resposta:
        return resposta
    else:
        return "Desculpe, não entendi a pergunta."


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)







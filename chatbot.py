from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Pares de perguntas e respostas

perguntas_respostas = {
    1: "Olá! Como posso ajudar você?",
    2: "Estou bem, obrigado por perguntar.",
    3: "Meu nome é Dira.",
    4: "Posso responder a perguntas simples.",
    5: "Tchau! Tenha um bom dia!"
}

Cumprimento = ["Olá", "oi", "e ai"," qual foi","fala"]


app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_question = data['question']
    resposta = responder_pergunta(user_question)
    return jsonify({'response': resposta})


def responder_pergunta(pergunta):
   
    tokens = word_tokenize(pergunta.lower())

    if(len(tokens) > 1):
        expectativa = (tokens[0] +" "+ tokens[1]) 
        if expectativa in Cumprimento:
            resposta = perguntas_respostas.get(1)      
    else:
        for word in tokens:
                
                if word in Cumprimento:
                    resposta = perguntas_respostas.get(1)        
                    if resposta:
                        return resposta
                    else:
                        return "Desculpe, não entendi a pergunta."
                    break


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

#v 1.5
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

# Carica le variabili d'ambiente
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Controllo della chiave API
if not API_KEY:
    raise ValueError("⚠️ ERRORE: API Key non trovata! Controlla il file .env e assicurati che DEEPSEEK_API_KEY sia impostata.")

app = Flask(__name__)

# Configura l'API
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/")
def index():
    return render_template("index.html")  # Carica la pagina HTML

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")  # Ottiene il messaggio dell'utente
    
    if not user_message:
        return jsonify({"response": "Errore: Messaggio non valido."}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        response = requests.post(API_URL, json=data, headers=headers)
        response.raise_for_status()  # Solleva un errore se la richiesta fallisce
        response_json = response.json()
        content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "Errore nella risposta dell'IA.")
        return jsonify({"response": content})
    except requests.exceptions.RequestException as e:
        return jsonify({"response": f"Errore nella richiesta API: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

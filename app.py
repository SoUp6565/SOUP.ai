from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Configura l'API
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"  # Tieni presente che dovresti proteggerla

@app.route("/")
def index():
    return render_template("index.html")  # Carica la pagina HTML

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")  # Ottiene il messaggio dell'utente

    # Controlla se la chiave API è disponibile
    if not API_KEY:
        return jsonify({"response": "Errore: API Key non configurata"}), 500

    # Prepara l'intestazione e il corpo della richiesta
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek/deepseek-chat:free",  # Usa il modello corretto
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(API_URL, json=data, headers=headers)

    # Gestione della risposta API (esattamente come il codice funzionante)
    if response.status_code == 200:
        response_json = response.json()
        content = response_json["choices"][0]["message"]["content"]
        return jsonify({"response": content})
    else:
        return jsonify({"response": f"Errore nell'API: {response.status_code} - {response.text}"})

if __name__ == "__main__":
    app.run(debug=True)

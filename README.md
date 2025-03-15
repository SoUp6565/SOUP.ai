# SOUP.ai - Chatbot basato su DeepSeek API

SOUP.ai è un chatbot avanzato che utilizza le API di DeepSeek per fornire risposte intelligenti e contestuali alle domande degli utenti. Con una semplice interfaccia, gli utenti possono digitare una domanda nella barra di input e ricevere una risposta immediata.

## 🚀 Funzionalità
- Interazione in linguaggio naturale
- Risposte rapide e contestuali
- Interfaccia semplice e intuitiva

## 🛠️ Tecnologie Utilizzate
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask/FastAPI)
- **API**: DeepSeek

## 📦 Installazione
1. **Clona il repository**
   ```bash
   git clone https://github.com/SoUp6565/SOUP.ai.git
   cd SOUP.ai
   ```
2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configura le API Key**
   - Crea un file `.env` nella root del progetto
   - Aggiungi la tua chiave API di DeepSeek:
     ```env
     DEEPSEEK_API_KEY=your_api_key_here
     ```
4. **Avvia il server**
   ```bash
   python app.py
   ```
5. **Apri il browser e accedi a:**
   ```
   http://127.0.0.1:5000
   ```

## 📌 Utilizzo
1. Scrivi la tua domanda nella barra di input.
2. Premi "Invia" e ricevi una risposta basata sull'IA di DeepSeek.

## 🛠️ Configurazione avanzata
Se vuoi personalizzare il comportamento del chatbot, modifica `config.py` per adattarlo alle tue esigenze.

## 🤝 Contributi
Se vuoi contribuire al progetto:
- Forka il repository
- Crea un branch con la tua modifica (`git checkout -b feature-nuova`)
- Effettua una pull request

## 📄 Licenza
Questo progetto è distribuito sotto licenza MIT.


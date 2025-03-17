# SOUP.ai - Chatbot basato su DeepSeek API

SOUP.ai è un chatbot avanzato che utilizza le API di DeepSeek per fornire risposte intelligenti e contestuali alle domande degli utenti. Con una semplice interfaccia, gli utenti possono digitare una domanda nella barra di input e ricevere una risposta immediata.

## 🚀 Funzionalità
- Interazione in linguaggio naturale
- Risposte rapide e contestuali
- Interfaccia semplice e intuitiva

## 🛠️ Tecnologie Utilizzate
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **API:** DeepSeek (tramite OpenRouter)

## 📦 Installazione

### 1️⃣ Clona il repository
Apri un terminale e clona il progetto dal repository GitHub:
```bash
git clone https://github.com/SoUp6565/SOUP.ai.git
cd SOUP.ai
```

### 2️⃣ Installa le dipendenze
Assicurati di avere **Python 3.13** installato, poi esegui:
```bash
pip install -r requirements.txt
```

### 3️⃣ Modifica la chiave API
Il chatbot utilizza le API di DeepSeek tramite OpenRouter. Nel file `app.py`, sostituisci la chiave API presente con la tua chiave personale.

### 4️⃣ Avvia il server Flask
Esegui il comando:
```bash
python app.py
```

Se tutto è configurato correttamente, dovresti vedere un messaggio simile a questo:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 5️⃣ Accedi all'interfaccia del chatbot
Apri il browser e vai su:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Ora puoi iniziare a interagire con SOUP.ai!

## 📌 Utilizzo
1. Scrivi la tua domanda nella barra di input.
2. Premi "Invia" e ricevi una risposta basata sull'IA di DeepSeek.
3. Continua la conversazione digitando nuove domande.

## 🛠️ Configurazione avanzata
Se vuoi personalizzare il comportamento del chatbot, puoi modificare `app.py` per:
- Cambiare il modello AI usato nelle richieste API.
- Personalizzare il layout modificando `index.html` e `style.css`.

## 🤝 Contributi
Se vuoi contribuire al progetto:
1. Forka il repository
2. Crea un branch con la tua modifica:
```bash
git checkout -b feature-nuova
```
3. Implementa le modifiche e committale:
```bash
git commit -m "Aggiunto supporto per nuova funzione"
```
4. Pusha il branch e crea una Pull Request.

## 📄 Licenza
Questo progetto è distribuito sotto licenza **MIT**.

---

Ora sei pronto per usare SOUP.ai! 🚀


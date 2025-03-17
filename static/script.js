document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.getElementById("chatBox");
    const userInput = document.getElementById("userInput");

    window.sendMessage = function() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Mostra il messaggio dell'utente nella chat
        appendMessage("user", message);
        userInput.value = "";

        // Invia il messaggio al server Flask
        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Mostra la risposta del bot
            appendMessage("bot", data.response);
        })
        .catch(error => console.error("Errore:", error));
    };

    // Permette di inviare con "Invio"
    window.handleKeyPress = function(event) {
        if (event.key === "Enter") sendMessage();
    };

    // Aggiunge un messaggio nella chat
    function appendMessage(role, text) {
        const msgDiv = document.createElement("div");
        msgDiv.classList.add("message", role);
        msgDiv.textContent = text;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scorrimento automatico
    }
});

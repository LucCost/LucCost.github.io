function sendMessage() {
    const message = document.getElementById('message').value;
    const serverResponse = document.getElementById('server-response');

    // Simulação de resposta do servidor
    if (message.trim() === "") {
        serverResponse.textContent = "Por favor, insira uma mensagem!";
    } else {
        serverResponse.textContent = "Mensagem enviada: " + message;
    }
}

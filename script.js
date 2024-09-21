document.getElementById("calcForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let valor1 = document.getElementById("valor1").value;
    let valor2 = document.getElementById("valor2").value;
    let operacao = document.getElementById("operacao").value;

    fetch('/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            valor1: valor1,
            valor2: valor2,
            operacao: operacao
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").innerHTML = "Resultado: " + data.resultado;
    })
    .catch(error => {
        document.getElementById("resultado").innerHTML = "Erro ao calcular.";
    });
});

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    valor1 = int(data['valor1'])
    valor2 = int(data['valor2'])
    operacao = data['operacao']
    
    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        resultado = valor1 / valor2
    else:
        return jsonify({"erro": "Operação inválida"}), 400
    
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)

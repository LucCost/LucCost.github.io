from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Verifica se os dados estão completos
        data = request.json
        
        # Verifica se as chaves existem e se são números válidos
        if 'valor1' not in data or 'valor2' not in data or 'operacao' not in data:
            return jsonify({"erro": "Dados incompletos"}), 400

        valor1 = float(data['valor1'])  # Convertendo para float para aceitar números decimais
        valor2 = float(data['valor2'])
        operacao = data['operacao']
        
        # Executa a operação
        if operacao == '+':
            resultado = valor1 + valor2
        elif operacao == '-':
            resultado = valor1 - valor2
        elif operacao == '*':
            resultado = valor1 * valor2
        elif operacao == '/':
            if valor2 == 0:  # Verifica se está dividindo por zero
                return jsonify({"erro": "Divisão por zero não é permitida"}), 400
            resultado = valor1 / valor2
        else:
            return jsonify({"erro": "Operação inválida"}), 400

        # Retorna o resultado
        return jsonify({"resultado": resultado})

    except ValueError:
        return jsonify({"erro": "Valores numéricos inválidos"}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

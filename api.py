from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiplicar', methods=['POST'])
def sumar():
    num1 = request.json['num1']
    num2 = request.json['num2']
    resultado = num1 * num2
    return jsonify({'resultado': resultado})

@app.route('/carne', methods=['GET'])
def info():
    return jsonify({'carnet:':202000194})

if __name__ == '__main__':
    app.run(debug=True)





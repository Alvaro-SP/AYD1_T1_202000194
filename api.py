from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/carne', methods=['GET'])
def info():
    return jsonify({'carnet:':202000194})

if __name__ == '__main__':
    app.run(debug=True)

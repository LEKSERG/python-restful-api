from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/check', methods=['GET'])
def check():
    return jsonify(datetime.now())


@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    print(result)
    return jsonify(result)

@app.route('/subt/<int:num1>/<int:num2>', methods=['GET'])
def subt(num1, num2):
    result = num1 - num2
    print(result)
    return jsonify(result)

@app.route('/div/<int:num1>/<int:num2>', methods=['GET'])
def div(num1, num2):
    result = num1 / num2
    print(result)
    return jsonify(result)

@app.route('/mult/<int:num1>/<int:num2>', methods=['GET'])
def mult(num1, num2):
    result = num1 * num2
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
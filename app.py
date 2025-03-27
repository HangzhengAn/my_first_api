from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    try:
        result = data['num1'] + data['num2']
        return jsonify({
            'status': 'success',
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': '欢迎使用我的API',
        'endpoints': ['/calculate']
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '8654351542:AAHgwkZhGyichKIS1APditSo-kVo1liLy9I')

@app.route('/bot/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print("Modtaget data:", data)
        response = requests.post('http://localhost:5001/handle_message', json=data).json()
        return jsonify(response)
    except Exception as e:
        print(f"Fejl: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
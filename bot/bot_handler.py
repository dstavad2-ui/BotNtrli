from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '8654351542:AAHgwkZhGyichKIS1APditSo-kVo1liLy9I')

def get_guide(substance):
    with open('customer/harm_reduction/data/guides.json') as f:
        guides = json.load(f)
    return guides.get(substance, "Guide not found.")

@app.route('/handle_message', methods=['POST'])
def handle_message():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    if text == '/start':
        response_text = "Velkommen til Naturlig AI Bot! Brug /help for hjælp."
    elif text == '/help':
        response_text = "Brug /start for at starte eller skriv en besked. Brug /guide <substance> for harm reduction guides."
    elif text.startswith('/guide'):
        substance = text.split()[1]
        response_text = get_guide(substance)
    else:
        response_text = f"Du skrev: {text}"

    send_message_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={response_text}"
    requests.get(send_message_url)

    return {'method': 'sendMessage', 'chat_id': chat_id, 'text': response_text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
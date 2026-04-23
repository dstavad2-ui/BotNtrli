#!/bin/bash

# Stop eventuelle kørende processer
pkill -f "python bot/bot_api.py"
pkill -f "python bot/bot_handler.py"
pkill ngrok

# Start Flask-serveren
echo "Starter Flask-serveren..."
python bot/bot_api.py &
PID_FLASK=$!

# Start bot handler
echo "Starter bot handler..."
python bot/bot_handler.py &
PID_HANDLER=$!

# Start ngrok
echo "Starter ngrok..."
./ngrok http 5000 &
PID_NGROK=$!

sleep 10

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

if [ -z "$NGROK_URL" ]; then
    echo "Kunne ikke hente ngrok URL. Tjek om ngrok kører korrekt."
    kill $PID_FLASK $PID_HANDLER $PID_NGROK
    exit 1
fi

curl -X POST "https://api.telegram.org/bot8654351542:AAHgwkZhGyichKIS1APditSo-kVo1liLy9I/setWebhook?url=$NGROK_URL/bot/webhook"

echo "Serveren kører på $NGROK_URL"
echo "Webhook er indstillet til din Telegram-bot."

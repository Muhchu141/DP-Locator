import os
import requests
from flask import Flask, request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"].strip()
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
PORT = int(os.environ.get("PORT", 10000))
PUBLIC_URL = os.environ.get("RENDER_EXTERNAL_URL", "").rstrip("/")

app = Flask(__name__)


def send_message(chat_id, text):
    response = requests.post(
        f"{BASE_URL}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=15,
    )
    response.raise_for_status()


@app.route("/")
def home():
    return "Kobaa DP Locator is running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(silent=True) or {}
    message = update.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if chat_id and text.startswith("/start"):
        send_message(
            chat_id,
            "Welcome to Kobaa DP Locator! Bot is online."
        )

    return "OK", 200


if PUBLIC_URL:
    result = requests.post(
        f"{BASE_URL}/setWebhook",
        json={"url": f"{PUBLIC_URL}/webhook"},
        timeout=15,
    )
    print("Webhook setup:", result.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
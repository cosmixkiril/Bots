
from flask import Flask, request
import telegram
import openai
import os

TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "mysecret")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

@app.route(f"/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text:
        user_text = update.message.text
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_text}]
            )
            reply = response['choices'][0]['message']['content']
        except Exception as e:
            reply = f"Ошибка: {e}"
        bot.send_message(chat_id=update.message.chat.id, text=reply)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Бот работает!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


### Инструкция по запуску Telegram-бота на Render.com

1. Зарегистрируйся на https://render.com (бесплатно).
2. Создай новый Web Service → выбери GitHub или ZIP загрузку.
3. Задай переменные окружения:
   - BOT_TOKEN = токен твоего Telegram-бота (от BotFather)
   - OPENAI_API_KEY = твой ключ OpenAI
   - WEBHOOK_SECRET = любое слово (например, "mysecret")

4. После запуска Render выдаст ссылку типа:
   https://example-bot.onrender.com

5. Установи Webhook для Telegram:
   Открой браузер и введи:
   https://api.telegram.org/bot<токен>/setWebhook?url=https://example-bot.onrender.com/<WEBHOOK_SECRET>

   Пример:
   https://api.telegram.org/bot7213821752:AAGJo53KAZiJwFVwgfzl_3p4BSkc-6Pzj68/setWebhook?url=https://example-bot.onrender.com/mysecret

6. Всё! Бот будет принимать сообщения и отвечать через ChatGPT.

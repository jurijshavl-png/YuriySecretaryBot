import os
# Обновление вручную для Render
import logging
import datetime
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_vilnius_time():
    tz = pytz.timezone("Europe/Vilnius")
    now = datetime.datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_mock_economics():
    return {
        "eur_usd": "1.0872 (↑)",
        "gold": "1964.30 $/oz (↓)",
        "silver": "23.12 $/oz (↑)"
    }

def get_mock_weather():
    return {
        "wind": "6.3 м/с SE",
        "pressure": "1012 hPa (↘ падает)",
        "temperature": "+18°C"
    }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time_now = get_vilnius_time()
    eco = get_mock_economics()
    weather = get_mock_weather()

    message = f"""✅ Бот активен
🕒 Время (Вильнюс): {time_now}

💱 Экономика:
EUR/USD: {eco['eur_usd']}
Золото: {eco['gold']}
Серебро: {eco['silver']}

🌦 Погода:
Температура: {weather['temperature']}
Ветер: {weather['wind']}
Давление: {weather['pressure']}
"""
    await update.message.reply_text(message)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

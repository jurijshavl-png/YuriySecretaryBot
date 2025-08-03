from telegram import Update
from telegram.ext import ContextTypes

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Пример заглушки — сюда вы можете подставить реальную логику
    await update.message.reply_text("🌤 Прогноз погоды: ясно, +22°C, ветер северо-западный 3 м/с.")

def register_weather_command(application):
    application.add_handler(CommandHandler("weather", weather_handler))

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Погода пока не подключена. В будущем будет прогноз и температура.")

def register_weather_command(app: Application):
    app.add_handler(CommandHandler("weather", weather_handler))

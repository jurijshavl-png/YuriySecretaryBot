from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands.calendar import calendar_command

import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
TIMEZONE = os.getenv("TZ", "Europe/Vilnius")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот активен. Введите команду.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("календарь", calendar_command))

    app.run_polling()

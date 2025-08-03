# bot.py

import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from commands.calendar import calendar_command
from commands.fishing import fishing_command
from commands.dog import dog_command
from commands.car import car_command
from commands.documents import documents_command
from commands.construction import construction_command
from commands.remind import remind_command

import os

OWNER_ID = int(os.getenv("OWNER_ID"))

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("Извините, бот предназначен только для владельца.")
        return
    await update.message.reply_text("Бот готов. Введите команду.")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN переменная окружения не установлена.")

    app = Application.builder().token(token).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("напомни", remind_command))
    app.add_handler(CommandHandler("рыбалка", fishing_command))
    app.add_handler(CommandHandler("собака", dog_command))
    app.add_handler(CommandHandler("авто", car_command))
    app.add_handler(CommandHandler("документы", documents_command))
    app.add_handler(CommandHandler("стройка", construction_command))
    app.add_handler(CommandHandler("календарь", calendar_command))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

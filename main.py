import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_config import TELEGRAM_BOT_TOKEN

# Импорт команд
from commands.fishing import fishing
from commands.car import car
from commands.dog import dog
from commands.documents import documents
from commands.construction import construction
from commands.reminder import reminder
from commands.weather import weather
from commands.gardening import gardening

from calendar.calendar import calendar_command, add_to_calendar_command

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте! Я ваш помощник.\n"
        "Доступные команды:\n"
        "/напомни — создать напоминание\n"
        "/рыбалка — прогноз клёва и погода\n"
        "/авто — информация по авто\n"
        "/собака — прививки и паспорт Стеллы\n"
        "/документы — список важных документов\n"
        "/стройка — статус ремонта\n"
        "/погода — погода по региону\n"
        "/сад — садовые работы\n"
        "/календарь — показать события\n"
        "/добавь_в_календарь — добавить в Google Календарь"
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("напомни", reminder))
    app.add_handler(CommandHandler("рыбалка", fishing))
    app.add_handler(CommandHandler("авто", car))
    app.add_handler(CommandHandler("собака", dog))
    app.add_handler(CommandHandler("документы", documents))
    app.add_handler(CommandHandler("стройка", construction))
    app.add_handler(CommandHandler("погода", weather))
    app.add_handler(CommandHandler("сад", gardening))
    app.add_handler(CommandHandler("календарь", calendar_command))
    app.add_handler(CommandHandler("добавь_в_календарь", add_to_calendar_command))

    app.run_polling()

if __name__ == '__main__':
    main()

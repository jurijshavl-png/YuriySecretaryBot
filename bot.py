from telegram.ext import ApplicationBuilder, CommandHandler
from commands.car import car_info
from commands.dog import dog_info
from commands.fishing import fishing_info
from commands.documents import documents_info
from commands.construction import construction_info
from commands.weather import weather_info
from commands.reminder import reminder_command
from commands.gardening import gardening_info
from calendar_commands.add_event import add_event

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Замените на свой токен

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("авто", car_info))
    application.add_handler(CommandHandler("собака", dog_info))
    application.add_handler(CommandHandler("рыбалка", fishing_info))
    application.add_handler(CommandHandler("документы", documents_info))
    application.add_handler(CommandHandler("стройка", construction_info))
    application.add_handler(CommandHandler("погода", weather_info))
    application.add_handler(CommandHandler("напомни", reminder_command))
    application.add_handler(CommandHandler("сад", gardening_info))
    application.add_handler(CommandHandler("добавь_в_календарь", add_event))  # ← новая команда

    application.run_polling()

if __name__ == "__main__":
    main()

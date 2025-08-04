from telegram.ext import Application, CommandHandler
from config import TELEGRAM_BOT_TOKEN

# Импорты всех команд
from commands.reminder import reminder_command
from commands.fishing import fishing_command
from commands.car import car_command
from commands.dog import dog_command
from commands.documents import documents_command
from commands.construction import construction_command
from commands.gardening import gardening_command
from commands.weather import weather_command

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрация команд
    application.add_handler(CommandHandler("напомни", reminder_command))
    application.add_handler(CommandHandler("рыбалка", fishing_command))
    application.add_handler(CommandHandler("авто", car_command))
    application.add_handler(CommandHandler("собака", dog_command))
    application.add_handler(CommandHandler("документы", documents_command))
    application.add_handler(CommandHandler("стройка", construction_command))
    application.add_handler(CommandHandler("сад", gardening_command))
    application.add_handler(CommandHandler("погода", weather_command))

    application.run_polling()

if __name__ == "__main__":
    main()

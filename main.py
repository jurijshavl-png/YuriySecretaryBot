import logging
from telegram.ext import Application

from config import TELEGRAM_BOT_TOKEN

# Импорт команд
from commands.dog import register_dog_command
from commands.car import register_car_command
from commands.documents import register_documents_command
from commands.fishing import register_fishing_command
from commands.construction import register_construction_command
from commands.gardening import register_gardening_command
from commands.reminder import register_reminder_command

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрация команд
    register_dog_command(application)
    register_car_command(application)
    register_documents_command(application)
    register_fishing_command(application)
    register_construction_command(application)
    register_gardening_command(application)
    register_reminder_command(application)

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()

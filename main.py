import logging
from telegram.ext import Application, CommandHandler
from commands.fishing import fishing_command
from commands.weather import weather_command
from commands.car import car_command
from commands.dog import dog_command
from commands.documents import documents_command
from commands.gardening import gardening_command
from commands.construction import construction_command
from commands.reminder import reminder_command

# Включение логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Создание приложения с вашим токеном
application = Application.builder().token("8473269472:AAHoJADfo_3JAC8FfPf2lwQFnWDIxzlzWn8").build()

# Регистрация команд
application.add_handler(CommandHandler("рыбалка", fishing_command))
application.add_handler(CommandHandler("погода", weather_command))
application.add_handler(CommandHandler("авто", car_command))
application.add_handler(CommandHandler("собака", dog_command))
application.add_handler(CommandHandler("документы", documents_command))
application.add_handler(CommandHandler("сад", gardening_command))
application.add_handler(CommandHandler("стройка", construction_command))
application.add_handler(CommandHandler("напомни", reminder_command))

# Запуск бота
if __name__ == "__main__":
    application.run_polling()

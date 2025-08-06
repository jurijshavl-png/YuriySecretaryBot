import logging
from telegram.ext import ApplicationBuilder
from commands.car import car_command
from commands.dog import dog_command
from commands.fishing import fishing_command
from commands.documents import documents_command
from commands.gardening import gardening_command
from commands.construction import construction_command
from commands.reminder import reminder_command
from commands.weather import weather_command

# Логирование (для отладки)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Создание приложения
application = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

# Регистрация команд
application.add_handler(car_command)
application.add_handler(dog_command)
application.add_handler(fishing_command)
application.add_handler(documents_command)
application.add_handler(gardening_command)
application.add_handler(construction_command)
application.add_handler(reminder_command)
application.add_handler(weather_command)

# Запуск бота
if __name__ == '__main__':
    application.run_polling()

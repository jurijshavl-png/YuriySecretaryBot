import asyncio
import logging
from telegram.ext import ApplicationBuilder

from commands.car import car_command
from commands.dog import dog_command
from commands.fishing import fishing_command
from commands.documents import documents_command
from commands.construction import construction_command
from commands.gardening import gardening_command
from commands.reminder import reminder_command
from weather import weather_command

BOT_TOKEN = "8473269472:AAHoJADfo_3JAC8FfPf2lwQFnWDIxzlzWn8"  

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(car_command)
    application.add_handler(dog_command)
    application.add_handler(fishing_command)
    application.add_handler(documents_command)
    application.add_handler(construction_command)
    application.add_handler(gardening_command)
    application.add_handler(reminder_command)
    application.add_handler(weather_command)

    await application.initialize()
    await application.start()
    print("Бот запущен и работает.")
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())

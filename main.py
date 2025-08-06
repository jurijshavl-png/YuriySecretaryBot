import os
import asyncio
from telegram.ext import ApplicationBuilder

from commands.car import get_handler as get_car_handler
from commands.dog import get_handler as get_dog_handler
from commands.fishing import get_handler as get_fishing_handler
from commands.documents import get_handler as get_documents_handler
from commands.construction import get_handler as get_construction_handler
from commands.weather import get_handler as get_weather_handler
from commands.gardening import get_handler as get_gardening_handler
from commands.reminder import get_handler as get_reminder_handler

TOKEN = os.getenv("BOT_TOKEN")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Add all command handlers
    application.add_handler(get_car_handler())
    application.add_handler(get_dog_handler())
    application.add_handler(get_fishing_handler())
    application.add_handler(get_documents_handler())
    application.add_handler(get_construction_handler())
    application.add_handler(get_weather_handler())
    application.add_handler(get_gardening_handler())
    application.add_handler(get_reminder_handler())

    # Start the bot
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())

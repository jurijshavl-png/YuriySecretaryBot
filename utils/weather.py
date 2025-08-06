import os
import aiohttp

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Kintai,LT&units=metric&lang=ru&appid={OPENWEATHER_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Ошибка при получении погоды: {response.status}")
            return await response.json()

def analyze_pressure_tendency(current_pressure: float, previous_pressure: float) -> str:
    if previous_pressure is None:
        return "нет данных"
    if current_pressure > previous_pressure:
        return "растёт"
    elif current_pressure < previous_pressure:
        return "падает"
    else:
        return "стабильно"
        from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    weather_data = await get_weather()
    temp = weather_data["main"]["temp"]
    pressure = weather_data["main"]["pressure"]
    await update.message.reply_text(
        f"🌡 Температура: {temp}°C\n"
        f"🔻 Давление: {pressure} hPa"
    )

weather_command = CommandHandler("погода", weather_handler)

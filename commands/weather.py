from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import requests
import os

# Используйте API OpenWeatherMap (https://openweathermap.org/) — необходимо создать свой API-ключ
OPENWEATHER_API_KEY = os.getenv("8882da2bdcb761fe898e4feca5b96f75") or "your_api_key_here"
LOCATION = "Ginduliai,LT"

def get_weather():
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
    )
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Не удалось получить данные о погоде."

    weather_description = data["weather"][0]["description"].capitalize()
    temperature = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    wind_speed = round(data["wind"]["speed"], 1)
    pressure = round(data["main"]["pressure"] * 0.75006)  # перевод в мм.рт.ст
    cloudiness = data["clouds"]["all"]

    advice = []
    if temperature < 0:
        advice.append("На улице мороз, оденьтесь теплее.")
    elif temperature > 25:
        advice.append("Жарко, пейте больше воды.")
    elif 5 <= temperature <= 15:
        advice.append("Свежо, возможно потребуется куртка.")

    if wind_speed > 8:
        advice.append("Сильный ветер, лучше избегать долгих прогулок.")

    if humidity > 80:
        advice.append("Влажность высокая, возможен туман.")

    result = (
        f"📍 <b>Погода в {LOCATION}:</b>\n"
        f"{weather_description}\n"
        f"🌡 Температура: {temperature}°C (ощущается как {feels_like}°C)\n"
        f"💨 Ветер: {wind_speed} м/с\n"
        f"☁️ Облачность: {cloudiness}%\n"
        f"💧 Влажность: {humidity}%\n"
        f"🔻 Давление: {pressure} мм рт. ст.\n\n"
    )
    if advice:
        result += "<b>Совет:</b> " + " ".join(advice)

    return result

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_weather(), parse_mode="HTML")

def get_handler() -> CommandHandler:
    return CommandHandler("погода", weather_command)

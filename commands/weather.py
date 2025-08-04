from telegram import Update
from telegram.ext import ContextTypes
import datetime

# Пример заглушки погоды (позже можно подключить реальный API, например OpenWeather)
def get_mock_weather():
    return {
        "location": "Kintai, Klaipėdos rajonas",
        "date": datetime.datetime.now().strftime("%d.%m.%Y"),
        "temperature": "+20°C",
        "wind": "Юго-западный, 4–6 м/с",
        "pressure": "1012 гПа",
        "humidity": "70%",
        "fishing_tip": (
            "В районе Kintai сегодня умеренный ветер и стабильное давление — "
            "отличные условия для ловли жереха и язя на утренней зорьке. "
            "Рекомендуем использовать воблеры ZipBaits и Megabass вдоль русла Minijos."
        )
    }

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    weather_data = get_mock_weather()
    message = (
        f"📍 Погода для региона: {weather_data['location']}\n"
        f"🗓 Дата: {weather_data['date']}\n"
        f"🌡 Температура: {weather_data['temperature']}\n"
        f"💨 Ветер: {weather_data['wind']}\n"
        f"🌬 Давление: {weather_data['pressure']}\n"
        f"💧 Влажность: {weather_data['humidity']}\n\n"
        f"🎣 Совет рыболову: {weather_data['fishing_tip']}"
    )
    await update.message.reply_text(message)
weather_command = weather

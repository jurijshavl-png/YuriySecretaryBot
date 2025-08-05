import requests
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes
from math import cos, sin, radians

# Координаты для Kintai (Minija)
LAT = 55.419
LON = 21.271
API_KEY = "YOUR_OPENWEATHER_API_KEY"  # ← ВСТАВЬТЕ ВАШ КЛЮЧ

# Предыдущие значения давления для анализа тенденции
previous_pressure = None

async def get_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}"
        f"&appid={API_KEY}&units=metric&lang=ru"
    )
    response = requests.get(url)
    data = response.json()
    return data

def analyze_pressure_tendency(current, previous):
    if previous is None:
        return "недоступна (недостаточно данных)"
    elif current > previous:
        return "растёт"
    elif current < previous:
        return "падает"
    else:
        return "стабильное"

def get_moon_phase():
    day_of_year = datetime.utcnow().timetuple().tm_yday
    synodic_month = 29.53058867
    moon_age = day_of_year % synodic_month

    if moon_age < 1:
        return "Новолуние 🌑"
    elif moon_age < 7.4:
        return "Растущая луна 🌒"
    elif moon_age < 14.8:
        return "Полнолуние 🌕"
    elif moon_age < 22.1:
        return "Убывающая луна 🌖"
    else:
        return "Новолуние 🌑"

def get_mock_water_level():
    # Здесь можно подключить реальный API или оставить имитацию
    return "Уровень воды в Минее: 148 см (нормально)"

def generate_fishing_advice(temp, pressure, wind_speed, cloudiness):
    species = []
    lures = []
    techniques = []

    # Примеры логики
    if 12 <= temp <= 20:
        species.append("голавль, язь, жерех, окунь")
        lures.append("воблеры 35–55 мм (ZipBaits Rigge, Megabass X-55)")
        techniques.append("апстрим, проводка вдоль струи")

    if temp < 10:
        species.append("форель, окунь")
        lures.append("тонущие воблеры, micro crank")
        techniques.append("медленная равномерная проводка")

    if wind_speed > 8:
        techniques.append("использовать огруженные приманки")
    if cloudiness > 70:
        techniques.append("использовать яркие цвета (mat tiger, chartreuse)")
    else:
        techniques.append("использовать натуральные цвета (silver, ghost minnow)")

    advice = (
        f"<b>Предполагаемая активная рыба:</b> {', '.join(set(species)) or 'данные отсутствуют'}\n"
        f"<b>Рекомендуемые приманки:</b> {', '.join(set(lures)) or 'уточните по условиям'}\n"
        f"<b>Техника ловли:</b> {', '.join(set(techniques)) or 'по ситуации'}"
    )
    return advice

async def fishing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global previous_pressure
    weather = await get_weather()

    temp = weather["main"]["temp"]
    pressure = weather["main"]["pressure"]
    wind_speed = weather["wind"]["speed"]
    wind_deg = weather["wind"]["deg"]
    cloudiness = weather["clouds"]["all"]

    pressure_tendency = analyze_pressure_tendency(pressure, previous_pressure)
    previous_pressure = pressure  # сохраняем текущее давление

    # Перевод ветра в направление
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    wind_dir_index = round(wind_deg / 45) % 8
    wind_direction = directions[wind_dir_index]

    # Луна и уровень воды
    moon_phase = get_moon_phase()
    water_level = get_mock_water_level()

    # Генерация рыболовных советов
    advice = generate_fishing_advice(temp, pressure, wind_speed, cloudiness)

        text = (
        f"<b>🌤 Погода в районе Kintai (река Миня):</b>\n"
        f"🌡 Температура: {temp:.1f} °C\n"
        f"☁️ Облачность: {cloudiness}%\n"
        f"💨 Ветер: {wind_speed:.1f} м/с, направление: {wind_direction}\n"
        f"📈 Давление: {pressure} гПа ({pressure_tendency})\n"
        f"🌙 Фаза луны: {moon_phase}\n"
        f"{water_level}\n\n"
        f"{advice}"
    )

    await update.message.reply_text(text, parse_mode="HTML")

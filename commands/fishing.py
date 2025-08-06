from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from utils.weather import get_weather, analyze_pressure_tendency
from utils.moon import get_moon_phase
from utils.water_level import get_mock_water_level


previous_pressure = 1013.0  # начальное значение по умолчанию


def generate_fishing_advice(temp, pressure, wind_speed, cloudiness):
    advice = "🎣 Рекомендации по рыбалке:\n"

    # Температура
    if temp < 5:
        advice += " - Рыба малоподвижна, пробуйте донные приманки.\n"
    elif temp < 15:
        advice += " - Оптимальная активность, подходят воблеры и блёсны.\n"
    else:
        advice += " - В тёплой воде рыба уходит в тень, пробуйте раннее утро или вечер.\n"

    # Давление
    if pressure < 1005:
        advice += " - Низкое давление, возможен слабый клёв.\n"
    elif pressure > 1020:
        advice += " - Высокое давление, рыба пассивна.\n"
    else:
        advice += " - Нормальное давление, шансы хорошие.\n"

    # Облачность
    if cloudiness > 70:
        advice += " - Пасмурно, рыба может быть ближе к поверхности.\n"
    elif cloudiness < 20:
        advice += " - Ясно, используйте приманки естественных цветов.\n"
    else:
        advice += " - Переменная облачность — универсальные условия.\n"

    # Ветер
    if wind_speed < 2:
        advice += " - Штиль — используйте лёгкие приманки.\n"
    elif wind_speed < 6:
        advice += " - Лёгкий ветер — отличное время для ловли.\n"
    else:
        advice += " - Сильный ветер — ищите укрытые участки реки.\n"

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
    previous_pressure = pressure

    # Направление ветра
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    wind_dir_index = round(wind_deg / 45) % 8
    wind_direction = directions[wind_dir_index]

    moon_phase = get_moon_phase()
    water_level = get_mock_water_level()

    advice = generate_fishing_advice(temp, pressure, wind_speed, cloudiness)

    text = (
        f"<b>🌤 Погода в районе Kintai (река Миня):</b>\n"
        f"🌡Температура: {temp:.1f} °C\n"
        f"☁Облачность: {cloudiness}%\n"
        f"💨Ветер: {wind_speed:.1f} м/с, направление: {wind_direction}\n"
        f"🧭Атм. давление: {pressure} гПа ({pressure_tendency})\n"
        f"🌙Фаза луны: {moon_phase}\n"
        f"🌊Уровень воды: {water_level}\n\n"
        f"{advice}"
    )

    await update.message.reply_text(text, parse_mode="HTML")


fishing_command = CommandHandler("fishing", fishing)


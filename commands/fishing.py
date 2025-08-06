from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.weather import get_weather
from utils.moon import get_moon_phase
from utils.water_level import get_mock_water_level
from utils.weather import analyze_pressure_tendency

previous_pressure = 1013  # default value


def generate_fishing_advice(temp, pressure, wind_speed, cloudiness):
    advice = ""

    if temp < 5:
        advice += "Холодно, рыба малоподвижна. Используйте медленные проводки и натуральные цвета приманок.\n"
    elif 5 <= temp <= 15:
        advice += "Комфортная температура. Хорошее время для ловли окуня и щуки. Приманки — воблеры ZipBaits, Megabass.\n"
    else:
        advice += "Тёплая погода. Активны жерех и язь. Используйте быстрые проводки и яркие приманки.\n"

    if pressure < 1005:
        advice += "Низкое давление — рыба пассивна. Лучше использовать приманки с сильной вибрацией.\n"
    elif pressure > 1020:
        advice += "Высокое давление — хорошая активность, особенно в утренние часы.\n"

    if wind_speed > 6:
        advice += "Сильный ветер. Рыба уходит в укрытия, стоит ловить у береговой растительности.\n"

    if cloudiness > 70:
        advice += "Пасмурно — используйте тёмные приманки.\n"
    else:
        advice += "Ясно — подойдут яркие и светлые приманки.\n"

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

    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    wind_dir_index = round(wind_deg / 45) % 8
    wind_direction = directions[wind_dir_index]

    moon_phase = get_moon_phase()
    water_level = get_mock_water_level()

    advice = generate_fishing_advice(temp, pressure, wind_speed, cloudiness)

    text = (
        f"<b>🌤 Погода в районе Kintai (река Миня):</b>\n"
        f"Температура: {temp:.1f} °C\n"
        f"Облачность: {cloudiness}%\n"
        f"Ветер: {wind_speed:.1f} м/с, направление: {wind_direction}\n"
        f"Атм. давление: {pressure} гПа ({pressure_tendency})\n"
        f"Фаза луны: {moon_phase}\n"
        f"Уровень воды: {water_level}\n\n"
        f"{advice}"
    )

    await update.message.reply_text(text, parse_mode="HTML")




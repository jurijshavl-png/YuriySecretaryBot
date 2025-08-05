from telegram import Update
from telegram.ext import ContextTypes
from utils.weather import get_weather
from utils.moon import get_moon_phase
from utils.water_level import get_mock_water_level

# Предыдущее давление для анализа тенденции
previous_pressure = None

def analyze_pressure_tendency(current, previous):
    if previous is None:
        return "нет данных"
    elif current > previous:
        return "растёт"
    elif current < previous:
        return "падает"
    else:
        return "стабильное"

def generate_fishing_advice(temp, pressure, wind_speed, cloudiness):
    species = []
    lures = []
    techniques = []

    if 14 <= temp <= 20:
        species.append("жерех")
        lures.append("воблеры ZipBaits Khamsin")
        techniques.append("быстрая проводка у поверхности")

    if 18 <= temp <= 24:
        species.append("язь")
        lures.append("Megabass Great Hunting")
        techniques.append("медленная проводка у кромки травы")

    if pressure > 1020:
        techniques.append("деликатная проводка на паузах")

    if wind_speed < 2:
        lures.append("поверхностные приманки")

    if cloudiness > 70:
        techniques.append("использовать яркие цвета (mat tiger, chartreuse)")
    else:
        techniques.append("использовать натуральные цвета (silver, ghost minnow)")

    advice = (
        f"<b>🎯 Предполагаемая активная рыба:</b> {', '.join(species) or 'данные отсутствуют'}\n"
        f"<b>🎣 Рекомендуемые приманки:</b> {', '.join(set(lures)) or 'уточните по условиям'}\n"
        f"<b>🧰 Техника ловли:</b> {', '.join(set(techniques)) or 'по ситуации'}"
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
    previous_pressure = pressure

    # Направление ветра (градусы в стороны света)
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    wind_dir_index = round(wind_deg / 45) % 8
    wind_direction = directions[wind_dir_index]

    moon_phase = get_moon_phase()
    water_level = get_mock_water_level()

    advice = generate_fishing_advice(temp, pressure, wind_speed, cloudiness)

    text = (
        f"<b>🌤️ Погода в районе Kintai (река Миня):</b>\n"
        f"🌡️Температура: {temp:.1f} °C\n"
        f"☁️Облачность: {cloudiness}%\n"
        f"💨Ветер: {wind_speed:.1f} м/с, направление: {wind_direction}\n"
        f"📈Давление: {pressure} гПа ({pressure_tendency})\n"
        f"🌕Фаза луны: {moon_phase}\n"
        f"🌊Уровень воды: {water_level}\n\n"
        f"{advice}"
    )

    await update.message.reply_text(text, parse_mode="HTML")

fishing_command = fishing

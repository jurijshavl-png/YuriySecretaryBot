from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import datetime

# Список приманок и целей
FISHING_TIPS = {
    "species": ["Окунь", "Щука", "Форель", "Жерех", "Язь"],
    "lures": [
        "🎣 ZipBaits Rigge 35F",
        "🎣 Megabass Great Hunting Minnow 48",
        "🎣 Pontoon21 CrackJack 38SP",
        "🎣 DUO Ryuki 45S",
        "🎣 Tiemco Sumari 50FS"
    ],
    "region": "Река Minija (регион Kintai)"
}

def format_fishing_info():
    today = datetime.date.today().strftime("%d.%m.%Y")
    tips = "\n".join(f"- {lure}" for lure in FISHING_TIPS["lures"])
    return (
        f"🎣 *План рыбалки на {today}*\n"
        f"- Регион: *{FISHING_TIPS['region']}*\n"
        f"- Целевые виды: {', '.join(FISHING_TIPS['species'])}\n\n"
        f"🧰 *Рекомендуемые приманки:*\n"
        f"{tips}\n\n"
        f"🌤 Погода и давление можно проверить командой /погода"
    )

async def fishing_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = format_fishing_info()
    await update.message.reply_text(text, parse_mode="Markdown")

def register_fishing_command(application):
    application.add_handler(CommandHandler("рыбалка", fishing_command))

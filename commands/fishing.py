from telegram import Update
from telegram.ext import ContextTypes

async def fishing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "🎣 *Прогноз клёва и погода для рыбалки*\n\n"
        "✅ Вода: стабильная\n"
        "✅ Ветер: слабый\n"
        "✅ Давление: нормальное\n\n"
        "🎯 Цели: жерех, голавль, форель\n"
        "🎣 Приманки: воблеры ZipBaits Rigge, Megabass X-55, блёсны Smith Pure 3.5g\n"
        "📍 Место: река Minija\n\n"
        "_Данные обновляются ежедневно._"
    )
    await update.message.reply_markdown_v2(message)
fishing_command = fishing

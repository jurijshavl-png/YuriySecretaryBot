from telegram import Update
from telegram.ext import ContextTypes

async def calendar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Это команда /календарь.\n"
        "Функции, связанные с Google Calendar, будут здесь.\n"
        "Например:\n"
        "– /добавь_в_календарь\n"
        "– /дела\n"
        "– /напомни встречу и т.д."
    )

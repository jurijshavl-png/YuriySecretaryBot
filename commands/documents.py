from telegram import Update
from telegram.ext import ContextTypes

async def documents(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "📁 *Документы Юрия*\n\n"
        "1. 📄 Паспорт моряка — [срок действия?]\n"
        "2. 📑 ISM manual — доступен в Telegram боте\n"
        "3. 🐶 EU Pet Passport (Стелла) — до 06.04.2028\n"
        "4. 📌 Прививки собаки — актуальны\n"
        "5. 🛠️ Документы по стройке — см. /стройка\n\n"
        "_Позже можно прикрепить PDF-файлы._"
    )
    await update.message.reply_markdown_v2(message)

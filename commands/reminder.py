import re
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

reminders = []

async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    pattern = r"/напомни\s+(.*?)\s+(\d{1,2}\s+\w+)"
    match = re.search(pattern, text)

    if match:
        task = match.group(1)
        date_str = match.group(2)
        try:
            date_obj = datetime.strptime(date_str, "%d %B")
            formatted_date = date_obj.strftime("%d %B")
            reminders.append((task, formatted_date))
            await update.message.reply_text(f"📌 Напоминание записано:\n«{task}» — {formatted_date}")
        except ValueError:
            await update.message.reply_text("❌ Неверный формат даты. Пример: /напомни заменить фильтр 1 октября")
    else:
        await update.message.reply_text("ℹ️ Пример: /напомни заменить фильтр 1 октября")

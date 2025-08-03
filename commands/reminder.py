from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from datetime import datetime
import json
import os

REMINDERS_FILE = "reminders.json"

def load_reminders():
    if os.path.exists(REMINDERS_FILE):
        with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_reminders(data):
    with open(REMINDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

async def reminder_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    message = " ".join(context.args)

    if not message:
        await update.message.reply_text("❗ Формат: `/напомни заменить фильтр 1 октября`", parse_mode="Markdown")
        return

    try:
        # Попробуем выделить дату из конца строки
        date_str = message.strip().split()[-2:]
        date_parsed = " ".join(date_str)
        reminder_date = datetime.strptime(date_parsed, "%d %B")

        # Остаток текста — это задача
        reminder_text = message.replace(date_parsed, "").strip()

        # Добавляем год, если не указан
        if reminder_date.year == 1900:
            reminder_date = reminder_date.replace(year=datetime.now().year)

        # Сохраняем
        reminders = load_reminders()
        if user_id not in reminders:
            reminders[user_id] = []
        reminders[user_id].append({
            "text": reminder_text,
            "date": reminder_date.strftime("%Y-%m-%d")
        })
        save_reminders(reminders)

        await update.message.reply_text(f"🔔 Напоминание сохранено: *{reminder_text}* на `{reminder_date.strftime('%d.%m.%Y')}`", parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка: убедитесь, что формат правильный (`/напомни заменить фильтр 1 октября`)")

def register_reminder_command(application):
    application.add_handler(CommandHandler("напомни", reminder_command))

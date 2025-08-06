from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import datetime
import asyncio

# Временное хранилище напоминаний (не сохраняется при перезапуске)
reminders = {}

async def reminder_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if len(context.args) < 2:
            await update.message.reply_text(
                "Использование: /напомни <через N сек/мин> <текст напоминания>\n"
                "Примеры:\n"
                "/напомни 10мин Полей сад\n"
                "/напомни 30сек Проверь куртку"
            )
            return

        time_str = context.args[0]
        reminder_text = " ".join(context.args[1:])

        # Распознавание времени
        if "мин" in time_str:
            delay = int(time_str.replace("мин", "")) * 60
        elif "сек" in time_str:
            delay = int(time_str.replace("сек", ""))
        else:
            await update.message.reply_text("Укажите время в формате, например, 10мин или 30сек.")
            return

        chat_id = update.effective_chat.id
        now = datetime.datetime.now().strftime("%H:%M:%S")
        await update.message.reply_text(f"Напоминание установлено ({now}). Я напомню через {time_str}.")

        # Планировка напоминания
        async def send_reminder():
            await asyncio.sleep(delay)
            await context.bot.send_message(chat_id=chat_id, text=f"⏰ Напоминание: {reminder_text}")

        asyncio.create_task(send_reminder())

    except Exception as e:
        await update.message.reply_text(f"Ошибка при создании напоминания: {e}")

def get_handler() -> CommandHandler:
    return CommandHandler("напомни", reminder_command)

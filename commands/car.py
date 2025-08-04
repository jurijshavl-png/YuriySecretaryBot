from telegram import Update
from telegram.ext import ContextTypes

async def car(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "🚗 *Информация об автомобиле Audi Q5 Sportback*\n\n"
        "• Последнее ТО: 2025-05-10\n"
        "• Следующее ТО: 2026-05-10\n"
        "• Состояние шин: летние\n"
        "• Текущий пробег: 5260 км\n"
        "• Напоминание: проверка давления в шинах раз в месяц\n\n"
        "_Все данные обновляются вручную._"
    )
    await update.message.reply_markdown_v2(message)
car_command = car

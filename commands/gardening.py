from telegram import Update, constants
from telegram.ext import ContextTypes, CommandHandler

async def gardening_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"<b>Садоводство</b>\n\n"
        f"<b>Плодовые деревья:</b>\n"
        f"• В июле–августе: полив при засухе, санитарная обрезка побегов\n"
        f"• Конец августа: начало подготовки к осенней подкормке\n\n"
        f"<b>Трава и газон:</b>\n"
        f"• Подстрижка 1 раз в 7–10 дней\n"
        f"• Подкормка каждые 3–4 недели минеральными удобрениями\n\n"
        f"<b>Сорняки:</b>\n"
        f"• Регулярное удаление вручную или точечная обработка гербицидами\n\n"
        f"<b>Ожидаемые задачи:</b>\n"
        f"• Август: сбор урожая, профилактика от вредителей, прореживание загущений\n"
        f"• Сентябрь: подготовка деревьев к зиме, мульчирование, обработка от грибков\n\n"
        f"<i>Подсказки по уходу также включаются в ежедневную сводку при подключении Google Calendar.</i>"
    )
    await update.message.reply_text(text, parse_mode=constants.ParseMode.HTML)

def get_handler() -> CommandHandler:
    return CommandHandler("gardening", gardening_command)

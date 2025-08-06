from telegram import Update, constants
from telegram.ext import ContextTypes, CommandHandler

async def construction_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"<b>Строительство и ремонт</b>\n\n"
        f"<b>Отопление:</b>\n"
        f"• Первый этаж: тёплые полы, управление через Salus\n"
        f"• Второй этаж: 4 радиатора с термоголовками Danfoss Eco Living\n"
        f"• Ванные комнаты: полы с ручной регулировкой\n\n"
        f"<b>Перегородки:</b>\n"
        f"• Отказ от стеклянной перегородки\n"
        f"• Выбраны вертикальные ламели с элементами матового золота\n\n"
        f"<b>Кухня:</b>\n"
        f"• Стеклянная витрина на краю кухни\n"
        f"• Поверхности: Dekton Morpheus\n"
        f"• Мебель: заказная, задержки по доставке\n\n"
        f"<b>Свет:</b>\n"
        f"• Установлены LED-профили с диммерами\n\n"
        f"<b>Прочее:</b>\n"
        f"• Управление отоплением и освещением в стадии настройки\n"
        f"• Подключение смарт-термостатов рассматривается\n\n"
        f"<i>Последнее обновление: август 2025</i>"
    )
    await update.message.reply_text(text, parse_mode=constants.ParseMode.HTML)

def get_handler() -> CommandHandler:
    return CommandHandler("construction", construction_command)

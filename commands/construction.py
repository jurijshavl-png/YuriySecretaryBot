from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import datetime

CONSTRUCTION_ITEMS = [
    {
        "item": "Стеклянная перегородка (ламели + матовое золото)",
        "status": "Ожидается установка",
        "eta": "2025-08-10",
        "store": "Gobana"
    },
    {
        "item": "Кухонная витрина с LED",
        "status": "Установлена",
        "eta": "2025-07-20",
        "store": "IKEA"
    },
    {
        "item": "Зеркало с подсветкой в ванную",
        "status": "Ожидается доставка",
        "eta": "2025-08-05",
        "store": "Topo Centras"
    }
]

def format_construction():
    today = datetime.date.today()
    lines = []
    for obj in CONSTRUCTION_ITEMS:
        eta_date = datetime.datetime.strptime(obj["eta"], "%Y-%m-%d").date()
        days_left = (eta_date - today).days
        eta_status = f"{days_left} дн. до установки" if days_left > 0 else "🔧 Срок прошёл"
        lines.append(
            f"- *{obj['item']}*\n"
            f"  Статус: _{obj['status']}_\n"
            f"  Срок: `{obj['eta']} ({eta_status})`\n"
            f"  Магазин: {obj['store']}\n"
        )
    return "\n".join(lines)

async def construction_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = (
        "🏗️ *Статус по стройке:*\n\n"
        f"{format_construction()}\n\n"
        "Обновление вручную или через Google Таблицы в будущем."
    )
    await update.message.reply_text(reply, parse_mode="Markdown")

def register_construction_command(application):
    application.add_handler(CommandHandler("стройка", construction_command))

from telegram import Update
from telegram.ext import ContextTypes

async def construction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "🏗️ *Статус строительных работ*\n\n"
        "• Стеклянная перегородка — заменена на вертикальные ламели ✅\n"
        "• Кухня — установлена (панель, Dekton, подсветка)\n"
        "• Шкаф в прихожей — ждем доставку\n"
        "• Ванная — полки и зеркало в процессе 🛁\n"
        "• Подсветка — работает, встраивание завершено\n"
        "• Стены — окрашены, стыки обработаны профилем\n\n"
        "📋 Подробнее — доступно по команде /документы или /напомни."
    )
    await update.message.reply_markdown_v2(message)
construction_command = construction

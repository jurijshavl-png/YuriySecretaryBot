from telegram import Update
from telegram.ext import ContextTypes

async def dog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "🐶 *Информация о собаке Стелле*\n\n"
        "• Порода: стандартный немецкий пинчер\n"
        "• Имя: Стелла\n"
        "• Возраст: 3 года\n"
        "• Вакцина от бешенства: Nobivac RL, действ. до 06.04.2028\n"
        "• DHPPi: Nobivac, действ. до 06.04.2026\n"
        "• Микрочип: 900215001869529\n"
        "• Паспорт ЕС: выдан в Литве\n\n"
        "_Все данные актуальны и соответствуют нормам ЕС._"
    )
    await update.message.reply_markdown_v2(message)

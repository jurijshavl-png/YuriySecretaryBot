from telegram import Update
from telegram.ext import ContextTypes

async def dog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "<b>🐶 Информация о собаке Стелле</b>\n\n"
        "<b>• Порода:</b> стандартный немецкий пинчер\n"
        "<b>• Имя:</b> Стелла\n"
        "<b>• Возраст:</b> 3 года\n"
        "<b>• Вакцина от бешенства:</b> Nobivac RL, действует до 06.04.2028\n"
        "<b>• DHPPI:</b> Nobivac, действует до 06.04.2026\n"
        "<b>• Микрочип:</b> 900215001869529\n"
        "<b>• Паспорт ЕС:</b> выдан в Литве\n\n"
        "<i>Все данные актуальны и соответствуют нормам ЕС.</i>"
    )
    await update.message.reply_text(message, parse_mode="HTML")

dog_command = dog

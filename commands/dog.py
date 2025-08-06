from telegram import Update, constants
from telegram.ext import ContextTypes, CommandHandler

# Статическая информация по собаке Стелле
DOG_INFO = {
    "name": "Стелла",
    "breed": "Стандартный немецкий пинчер, рыжий окрас",
    "age": "3 года",
    "passport": "EU Pet Passport, выдан в Литве",
    "microchip": "900215001869529 (установлен 14.03.2022)",
    "vaccinations": {
        "rabies": {
            "vaccine": "Nobivac RL",
            "date": "06.04.2025",
            "valid_until": "06.04.2028",
            "vet": "Aurėja Stanislauskaitė"
        },
        "DHPPi": {
            "vaccine": "Nobivac DHPPi",
            "date": "06.04.2025",
            "valid_until": "06.04.2026"
        }
    }
}

async def dog_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"<b>Информация о собаке</b>\n\n"
        f"<b>Имя:</b> {DOG_INFO['name']}\n"
        f"<b>Порода:</b> {DOG_INFO['breed']}\n"
        f"<b>Возраст:</b> {DOG_INFO['age']}\n\n"
        f"<b>Паспорт:</b> {DOG_INFO['passport']}\n"
        f"<b>Микрочип:</b> {DOG_INFO['microchip']}\n\n"
        f"<b>Прививка от бешенства:</b>\n"
        f"• Вакцина: {DOG_INFO['vaccinations']['rabies']['vaccine']}\n"
        f"• Дата: {DOG_INFO['vaccinations']['rabies']['date']}\n"
        f"• Действительна до: {DOG_INFO['vaccinations']['rabies']['valid_until']}\n"
        f"• Врач: {DOG_INFO['vaccinations']['rabies']['vet']}\n\n"
        f"<b>Комплексная прививка (DHPPi):</b>\n"
        f"• Вакцина: {DOG_INFO['vaccinations']['DHPPi']['vaccine']}\n"
        f"• Дата: {DOG_INFO['vaccinations']['DHPPi']['date']}\n"
        f"• Действительна до: {DOG_INFO['vaccinations']['DHPPi']['valid_until']}"
    )
    await update.message.reply_text(text, parse_mode=constants.ParseMode.HTML)

def get_handler() -> CommandHandler:
    return CommandHandler("dog", dog_command)

from telegram import Update, constants
from telegram.ext import ContextTypes, CommandHandler

async def documents_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"<b>Документы пользователя</b>\n\n"
        f"<b>1. Паспорт собаки (Стелла):</b>\n"
        f"• EU Pet Passport, выдан в Литве\n"
        f"• Микрочип: 900215001869529\n"
        f"• Вакцина от бешенства: Nobivac RL (06.04.2025 — 06.04.2028)\n"
        f"• Комплексная вакцина DHPPi: Nobivac (06.04.2025 — 06.04.2026)\n\n"
        f"<b>2. Автомобиль (Audi Q5 Sportback 2023):</b>\n"
        f"• VIN, регистрация: есть\n"
        f"• Владелец: Юрий, Литва\n"
        f"• Полный комплект документов, страхование КАСКО и ОСАГО\n\n"
        f"<b>3. Документы капитана:</b>\n"
        f"• Действующие сертификаты и лицензии\n"
        f"• Регулярные проверки и медосмотры\n"
        f"• Работа под флагом Германии, компания Hapag-Lloyd\n\n"
        f"<i>Все документы хранятся в оригинале у пользователя.</i>"
    )
    await update.message.reply_text(text, parse_mode=constants.ParseMode.HTML)

def get_handler() -> CommandHandler:
    return CommandHandler("documents", documents_command)

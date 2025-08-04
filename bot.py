from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN

def get_application() -> Application:
    """
    Создаёт и возвращает Telegram Bot Application.
    Используется в main.py для запуска и регистрации команд.
    """
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    return application

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN
from commands.reminder import reminder_command
from commands.fishing import fishing_command
from commands.car import car_command
from commands.dog import dog_command
from commands.documents import documents_command
from commands.construction import construction_command
from commands.gardening import gardening_command
from commands.weather import weather_command

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["/weather", "/fishing"],
        ["/dog", "/car"],
        ["/documents", "/construction"],
        ["/gardening", "/napomni"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Выберите команду:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("napomni", reminder_command))
    application.add_handler(CommandHandler("fishing", fishing_command))
    application.add_handler(CommandHandler("car", car_command))
    application.add_handler(CommandHandler("dog", dog_command))
    application.add_handler(CommandHandler("documents", documents_command))
    application.add_handler(CommandHandler("construction", construction_command))
    application.add_handler(CommandHandler("gardening", gardening_command))
    application.add_handler(CommandHandler("weather", weather_command))

    application.run_polling()

if __name__ == "__main__":
    main()

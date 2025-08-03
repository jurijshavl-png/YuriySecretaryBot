from telegram import Update
from telegram.ext import ContextTypes

# Данные о техническом обслуживании и пробеге — можно позже заменить на чтение из базы данных или файла
CAR_INFO = {
    "last_service_date": "2025-05-10",
    "next_tire_change": "2025-10-15",
    "current_mileage_km": 5260,
    "oil_change_km_interval": 15000,
}

def format_car_info():
    last_service = CAR_INFO["last_service_date"]
    next_tires = CAR_INFO["next_tire_change"]
    mileage = CAR_INFO["current_mileage_km"]
    next_oil_change = mileage + CAR_INFO["oil_change_km_interval"]
    return (
        f"🚗 *Информация об автомобиле:*\n"
        f"- Последнее ТО: *{last_service}*\n"
        f"- Смена шин: *{next_tires}*\n"
        f"- Текущий пробег: *{mileage} км*\n"
        f"- Следующая замена масла на ~*{next_oil_change} км*"
    )

async def car_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = format_car_info()
    await update.message.reply_text(text, parse_mode="Markdown")

def register_car_command(application):
    application.add_handler(CommandHandler("авто", car_command))

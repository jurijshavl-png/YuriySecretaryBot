from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def car_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "<b>Your Car Information:</b>\n\n"
        "<b>Model:</b> Audi Q5 Sportback 2023\n"
        "<b>Engine:</b> 2.0 TFSI (1984 cc), 195 kW\n"
        "<b>Mileage:</b> 5,260 km\n"
        "<b>Registration:</b> Lithuania 🇱🇹\n\n"
        "<b>Features:</b>\n"
        "• Virtual Cockpit\n"
        "• Audi Sound System\n"
        "• 3-zone Climate Control\n"
        "• Heated and Electrically Adjustable Sport Seats\n"
        "• Lane Change Assist & Parking Assist\n"
        "• Auto-dimming Mirrors\n"
        "• Cruise Control with Speed Limiter\n"
        "• High Beam Assist\n"
        "• Pre Sense Rear\n"
        "• 19-inch wheels (235/55 R19)\n\n"
        "<b>Interior:</b> Black with gray accents, Dinamica seats with 'S' embossing\n"
        "<b>Exterior:</b> Mythos Black Metallic\n"
        "<b>Others:</b> Illuminated door sills, stainless steel pedals, aluminum roof rails\n"
        "<b>Manual:</b> Available in Lithuanian\n"
    )
    await update.message.reply_text(message, parse_mode="HTML")

def get_handler():
    return CommandHandler("car", car_command)

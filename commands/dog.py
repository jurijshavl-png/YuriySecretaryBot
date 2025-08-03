from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

# Данные собаки — можно позже сделать обновляемыми из базы
DOG_INFO = {
    "name": "Стелла",
    "breed": "Стандартный немецкий пинчер",
    "age": "3 года",
    "chip": "900215001869529",
    "passport_issued": "Литва, EU Pet Passport",
    "rabies_vaccine": {
        "vaccine": "Nobivac RL",
        "date": "2025-04-06",
        "valid_until": "2028-04-06",
        "active_from": "2025-04-27"
    },
    "complex_vaccine": {
        "vaccine": "Nobivac DHPPi",
        "date": "2025-04-06",
        "valid_until": "2026-04-06"
    },
    "vet": "Aurėja Stanislauskaitė, PETCITY, Клайпеда"
}

def format_dog_info():
    r = DOG_INFO["rabies_vaccine"]
    c = DOG_INFO["complex_vaccine"]
    return (
        f"🐶 *Информация о собаке*\n"
        f"- Имя: *{DOG_INFO['name']}*\n"
        f"- Порода: *{DOG_INFO['breed']}*, возраст: *{DOG_INFO['age']}*\n"
        f"- Чип: `{DOG_INFO['chip']}`\n"
        f"- Паспорт: *{DOG_INFO['passport_issued']}*\n\n"
        f"💉 *Прививки:*\n"
        f"- Бешенство: *{r['vaccine']}* — {r['date']} (действует с {r['active_from']} до {r['valid_until']})\n"
        f"- DHPPi: *{c['vaccine']}* — {c['date']} (до {c['valid_until']})\n\n"
        f"👩‍⚕️ Ветеринар: {DOG_INFO['vet']}"
    )

async def dog_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = format_dog_info()
    await update.message.reply_text(text, parse_mode="Markdown")

def register_dog_command(application):
    application.add_handler(CommandHandler("собака", dog_command))

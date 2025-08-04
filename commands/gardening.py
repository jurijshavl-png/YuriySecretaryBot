from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

async def gardening(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now()
    month = now.strftime("%B")
    
    recommendations = {
        "March": "🌱 Март: обрезка плодовых деревьев, обработка от вредителей.",
        "April": "🌷 Апрель: посадка яблонь, груш, опрыскивание от грибков.",
        "May": "🌼 Май: подкормка, полив, защита от тли.",
        "June": "🌞 Июнь: прореживание завязей, контроль за поливом.",
        "July": "🍒 Июль: сбор урожая, защита от засухи.",
        "August": "🍏 Август: обрезка побегов, борьба с болезнями.",
        "September": "🍂 Сентябрь: посадка новых саженцев, уборка листьев.",
        "October": "🌳 Октябрь: перекопка почвы, мульчирование.",
        "November": "❄️ Ноябрь: утепление корней, чистка инвентаря.",
        "December": "🌨️ Декабрь: подготовка планов на сезон.",
        "January": "📋 Январь: проверка хранения урожая, инвентарь.",
        "February": "✂️ Февраль: подготовка к обрезке, проверка садового инструмента."
    }

    recommendation = recommendations.get(month, "🌿 Нет данных для текущего месяца.")
    await update.message.reply_text(f"🪴 Садовые работы на {month}:\n{recommendation}")

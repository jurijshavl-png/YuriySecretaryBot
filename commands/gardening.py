from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from datetime import datetime

# Простая логика по времени года
def get_seasonal_tips(month):
    tips = {
        1: "🌱 Январь: отдых сада. Проверяйте, не повреждены ли стволы и ветки от снега или мороза.",
        2: "🌱 Февраль: защита от грызунов, подготовка к обрезке.",
        3: "✂️ Март: начните обрезку деревьев до начала сокодвижения. Проверьте состояние газона.",
        4: "🌿 Апрель: удобрения для сада, стрижка газона, посадка новых саженцев.",
        5: "🌼 Май: борьба с вредителями, полив и мульчирование. Газон активно растёт — косите регулярно.",
        6: "🍒 Июнь: подкормка, защита от болезней. Сбор первых ягод.",
        7: "🌞 Июль: регулярный полив, обработка от вредителей. Косите траву при необходимости.",
        8: "🍎 Август: сбор урожая, санитарная обрезка.",
        9: "🍂 Сентябрь: подготовка к осени, посадка новых деревьев и кустов.",
        10: "🍁 Октябрь: уборка листьев, влагозарядковый полив.",
        11: "❄️ Ноябрь: побелка деревьев, укрытие молодых саженцев.",
        12: "❄️ Декабрь: контроль за состоянием укрытий и снегозадержание.",
    }
    return tips.get(month, "Нет данных по текущему месяцу.")

async def gardening_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now()
    tips = get_seasonal_tips(now.month)
    await update.message.reply_text(f"🧤 Рекомендации по саду на *{now.strftime('%B')}*:\n\n{tips}", parse_mode="Markdown")

def register_gardening_command(application):
    application.add_handler(CommandHandler("сад", gardening_command))

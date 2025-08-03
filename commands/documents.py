from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import datetime

DOCUMENTS = [
    {
        "name": "Паспорт моряка",
        "expires": "2026-02-15",
        "file": "📄 pasport_moryaka.pdf"
    },
    {
        "name": "ISM Manual",
        "expires": "2025-12-01",
        "file": "📄 ism_manual.pdf"
    },
    {
        "name": "Прививки собаки (Stella)",
        "expires": "2028-04-06",
        "file": "📄 vet_passport_stella.pdf"
    },
    {
        "name": "Сертификат вакцинации от бешенства",
        "expires": "2028-04-06",
        "file": "📄 rabies_certificate.pdf"
    }
]

def format_documents():
    today = datetime.date.today()
    lines = []
    for doc in DOCUMENTS:
        exp_date = datetime.datetime.strptime(doc["expires"], "%Y-%m-%d").date()
        days_left = (exp_date - today).days
        status = f"✅ Действует ({days_left} дн.)" if days_left > 0 else "⚠️ Истёк"
        lines.append(f"- *{doc['name']}* — {status}\n  {doc['file']}")
    return "\n\n".join(lines)

async def documents_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = (
        "📂 *Важные документы:*\n\n"
        f"{format_documents()}\n\n"
        "Для загрузки новых файлов или актуализации сроков — используйте Google Drive или ручную настройку."
    )
    await update.message.reply_text(reply, parse_mode="Markdown")

def register_documents_command(application):
    application.add_handler(CommandHandler("документы", documents_command))

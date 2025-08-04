from telegram import Update
from telegram.ext import ContextTypes
from calendar_commands.google_auth import get_calendar_service

async def add_event(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    service = get_calendar_service()
    event = {
        'summary': 'Test Event',
        'start': {'dateTime': '2025-08-05T10:00:00+03:00'},
        'end': {'dateTime': '2025-08-05T11:00:00+03:00'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
    await update.message.reply_text("Событие добавлено в Google Calendar.")

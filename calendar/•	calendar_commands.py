from telegram import Update
from telegram.ext import ContextTypes
from calendar.google_auth import get_calendar_service

async def add_event(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    service = get_calendar_service()
    event = {
        'summary': 'Test Event',
        'start': {'dateTime': '2025-08-04T10:00:00+03:00'},
        'end': {'dateTime': '2025-08-04T11:00:00+03:00'},
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    await update.message.reply_text(f"Событие создано: {event.get('htmlLink')}")

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from calendar_commands.google_auth import authenticate_google
from googleapiclient.discovery import build

import datetime


async def add_event_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Добавляет событие в Google Calendar"""
    try:
        creds = authenticate_google()
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow()
        event = {
            'summary': 'Тестовое событие',
            'start': {
                'dateTime': (now + datetime.timedelta(hours=1)).isoformat() + 'Z',
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (now + datetime.timedelta(hours=2)).isoformat() + 'Z',
                'timeZone': 'UTC',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        await update.message.reply_text(f"Событие добавлено: {event.get('htmlLink')}")

    except Exception as e:
        await update.message.reply_text(f"Ошибка при добавлении события: {str(e)}")


def register_add_event_command(application):
    application.add_handler(CommandHandler("добавь_в_календарь", add_event_command))

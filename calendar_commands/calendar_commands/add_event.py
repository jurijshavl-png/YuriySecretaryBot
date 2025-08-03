from googleapiclient.discovery import build
from datetime import datetime, timedelta
from .google_auth import get_credentials

def add_event_to_calendar(summary: str, description: str, date_str: str):
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    event_start = datetime.strptime(date_str, "%Y-%m-%d")
    event_end = event_start + timedelta(hours=1)

    event = {
        "summary": summary,
        "description": description,
        "start": {
            "dateTime": event_start.isoformat(),
            "timeZone": "Europe/Vilnius",
        },
        "end": {
            "dateTime": event_end.isoformat(),
            "timeZone": "Europe/Vilnius",
        },
    }

    created_event = service.events().insert(calendarId="primary", body=event).execute()
    return created_event.get("htmlLink")

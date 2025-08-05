from datetime import datetime
import math

def get_moon_phase():
    """
    Возвращает фазу луны в виде строки (например, "Полнолуние", "Растущая", и т.д.)
    Используется упрощённый алгоритм.
    """
    now = datetime.utcnow()
    year = now.year
    month = now.month
    day = now.day

    if month < 3:
        year -= 1
        month += 12

    a = math.floor(year / 100)
    b = 2 - a + math.floor(a / 4)
    jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + b - 1524.5
    days_since_new = jd - 2451549.5
    new_moons = days_since_new / 29.53058867
    phase_index = int((new_moons % 1) * 8 + 0.5) % 8

    phases = [
        "Новолуние",
        "Молодая луна",
        "Первая четверть",
        "Растущая луна",
        "Полнолуние",
        "Убывающая луна",
        "Последняя четверть",
        "Старая луна"
    ]

    return phases[phase_index]

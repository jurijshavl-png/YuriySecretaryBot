from .weather import register_weather_command
from .economy import register_economy_command
from .car import register_car_command
from .dog import register_dog_command
from .documents import register_documents_command
from .fishing import register_fishing_command
from .gardening import register_gardening_command
from .reminder import register_reminder_command
from .construction import register_construction_command

def register_commands(bot):
    register_weather_command(bot)
    register_economy_command(bot)
    register_car_command(bot)
    register_dog_command(bot)
    register_documents_command(bot)
    register_fishing_command(bot)
    register_gardening_command(bot)
    register_reminder_command(bot)
    register_construction_command(bot)

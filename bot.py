from bot import bot
from commands import register_commands

if __name__ == "__main__":
    register_commands(bot)
    bot.run_polling()

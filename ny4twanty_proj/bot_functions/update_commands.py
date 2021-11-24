import json

import requests
from telebot.types import BotCommand

from ny4twanty_proj.settings import TELEGRAM_URL, NY4TWANTY_BOT_TOKEN


def set_my_commands(commands):
    data = {
        "commands": commands,
    }
    response = requests.post(
        f"{TELEGRAM_URL}{NY4TWANTY_BOT_TOKEN}/setMyCommands", data=data
    )

    print(response.text)


commands = json.dumps([  # Edit here
    BotCommand(command='change_keyboard', description='Змінити клавіатуру').to_dict(),
    BotCommand(command='start', description='Почати').to_dict(),
])

set_my_commands(commands=commands)


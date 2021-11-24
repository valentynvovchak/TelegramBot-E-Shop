import requests

from ny4twanty_proj.settings import TELEGRAM_URL, NY4TWANTY_BOT_TOKEN


def change_keyboard():
    data = {
        # "commands": commands,
    }
    response = requests.post(
        f"{TELEGRAM_URL}{NY4TWANTY_BOT_TOKEN}/setMyCommands", data=data
    )

    print(response)

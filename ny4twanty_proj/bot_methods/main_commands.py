import json

import requests
from telebot.types import InlineKeyboardButton
from telebot import types

from ny4twanty_proj.helpers import write_json
from ny4twanty_proj.settings import NY4TWANTY_BOT_TOKEN, URL
from ny4twanty_proj.settings import TELEGRAM_URL


def send_message(message, chat_id, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    if reply_markup:
        data['reply_markup'] = reply_markup.to_json()

    response = requests.post(
        URL+"sendMessage", data=data
    )

    # write_json('message_with_markup', response)

    print(response)
git

def del_message(chat_id, message_id):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }
    response = requests.post(
        URL+"deleteMessage", data=data
    )

    # write_json('message_with_markup', response)

    print(response.text)


def send_photo(photo, chat_id, caption=None, reply_markup=None, reply_to=None, photo_type_fid=False):

    data = {
        "chat_id": chat_id,
        # "photo": 'AgACAgIAAxkBAANeYYf34CII_FaDjEOZRN1VJszQgxoAAse2MRsUr0FITJ7YQQQwIasBAAMCAAN5AAMiBA',
        "parse_mode": 'MarkdownV2',
        "allow_sending_without_reply": True,
    }
    if reply_markup:
        data['reply_markup'] = reply_markup.to_json()

    if reply_to:
        data['reply_to_message_id'] = reply_to

    if caption:
        data["caption"] = caption

    if photo_type_fid:
        data['photo'] = photo
    else:
        try:
            with open(photo, "rb") as image_file:
                response = requests.post(
                    URL+"sendPhoto", data=data, files={"photo": image_file}
                )

            # write_json('temp_bot_message', response)
            print(response)
        except Exception as e:
            print(e)

        # self.send_photo(
        #     caption='_Лови_ _*Аню*_',
        #     chat_id=t_chat["id"],
        #     reply_to=t_message["message_id"]
        # )


def get_sticker_set(name: str):
    data = {
        "name": name,
    }
    response = requests.post(
        URL+"getStickerSet", data=data
    )

    write_json('received_sticker_set', response)

    print(response)


def send_sticker(chat_id, sticker, reply_markup=None):

    data = {
        "chat_id": chat_id,
        "sticker": sticker,
    }

    if reply_markup:
        data['reply_markup'] = reply_markup.to_json(),

    response = requests.post(
        URL+"sendSticker", data=data
    )

    # write_json('send_sticker', response)

    print(response)


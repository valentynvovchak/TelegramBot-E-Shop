from ny4twanty_proj.bot.static import START_TEXT, MAIN_KEYBOARD, CATALOG_TEXT, catalog_
from ny4twanty_proj.bot_methods.main_commands import send_message


def handle_messages(data):

    # collecting data
    message = data['message']
    chat_id = message['chat']['id']
    username = None
    first_name = None
    if "first_name" in message['chat']:
        first_name = message['chat']['first_name']
    if "last_name" in message['chat']:
        last_name = message['chat']['last_name']
    if "username" in message['chat']:
        username = message['chat']['username']
    if "text" in data['message']:
        text_mess = data['message']['text']
    else:
        send_message(message='Якась незрозуміла проблема. Немає тексту повідомлення.', chat_id=chat_id)
        return "ok", 200

    # handling commands
    if text_mess == '/start':
        send_message(
            message=START_TEXT.format(username=(username or first_name)),
            chat_id=chat_id,
            reply_markup=MAIN_KEYBOARD
        )

    if text_mess == '📝 Каталог':
        send_message(
            message=CATALOG_TEXT.format(username=(username or first_name)),
            chat_id=chat_id,
            reply_markup=catalog_()
        )
        return 'ok', 200

    if text_mess == '🛒 Кошик':
        return 'ok', 200

    if text_mess == '⚙️Профіль':
        return 'ok', 200


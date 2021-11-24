import json

import telebot
from django.http import JsonResponse
from django.views import View

from ny4twanty_proj.bot_methods.main_commands import send_message, get_sticker_set, send_sticker, del_message
from .bot.callback_queries import handle_callback_queries
from .bot.messages import handle_messages
from .models import Chat

from .settings import NY4TWANTY_BOT_TOKEN

client = telebot.TeleBot(token=NY4TWANTY_BOT_TOKEN)
# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/


class RouterView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        with open('test_temp_files/temp.json', 'w') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

        if data.get("message"):
            message = data['message']

            text = message.get('text')
            if text:
                handle_messages(data)  # Опрацювати текстове повідомлення
            else:
                send_message(message='Прийшли непотрібні дані. В повідомленні немає тексту.', chat_id=782774390)

        elif data.get("callback_query"):
            message = data['callback_query'].get('message')

            if message:
                message_id = message.get('message_id')
                if message_id:
                    chat_id = message['chat']['id']
                    del_message(chat_id=chat_id, message_id=message_id)

            handle_callback_queries(data)  # Опрацювати колбек

        else:
            send_message(message='Прийшли непотрібні дані. Це ні не повідомлення, ні не колбек.', chat_id=782774390)

        # sticker="CAACAgIAAxUAAWGIHqh4Dh2j075bjBzruyFuYUXhAALTDgACoyLZSWJiZe_P-CSjIgQ"

        return JsonResponse({"ok": "POST request processed"})



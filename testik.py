
# GET CALLBACK QUERY
# if data.get('callback_query'):
#     callback_query = data["callback_query"]
#     print("id:", callback_query.get('id'))
#     print("message_id:", callback_query['message'].get('message_id'))
#     print("chat_id:", callback_query['message']['chat']['id'])
#     print("data:", callback_query['data'])

# SEND PHOTO --------------------------------------
# @staticmethod
# def send_photo(caption, chat_id, reply_to):
#     # sendPhoto
#
#     data = {
#         "chat_id": chat_id,
#         # "photo": 'AgACAgIAAxkBAANeYYf34CII_FaDjEOZRN1VJszQgxoAAse2MRsUr0FITJ7YQQQwIasBAAMCAAN5AAMiBA',
#         "caption": caption,
#         # "temp": '*bold _italic bold ~italic bold strikethrough~ __underline italic bold___ bold*',
#         "parse_mode": 'MarkdownV2',
#         "reply_to_message_id": reply_to,
#         "allow_sending_without_reply": True,
#     }
#
#     with open('/home/valya/Pictures/Anna/6.jpg', "rb") as image_file:
#         response = requests.post(
#             f"{TELEGRAM_URL}{NY4TWANTY_BOT_TOKEN}/sendPhoto", data=data, files={"photo": image_file}
#         )
#
        # with open('temp_bot_message.json', 'w') as file:
        #     file.write(json.dumps(json.loads(response.text), ensure_ascii=False, indent=4))

#         print(response)

#         self.send_photo(
#             caption='_Лови_ _*Аню*_',
#             chat_id=t_chat["id"],
#             reply_to=t_message["message_id"]
#         )
# END SEND PHOTO --------------------------------------

# json.dumps on telebot_api types !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# self.set_my_commands(json.dumps([
#     BotCommand(command='sticker', description='Відправити стікер').to_dict(),
#     BotCommand(command='add_sticker', description='Додаткова команда відправити стікер').to_dict()
# ]))

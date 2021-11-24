from ny4twanty_proj.bot.static import (
    MAIN_MENU_TEXT,
    MAIN_MENU_KEYBOARD,
    CATALOG_TEXT,
    subcategory_markup,
    prod_list_markup, PROD_DETAIL_MESSAGE, prod_detail_markup, catalog_
)

from ny4twanty_proj.bot_methods.main_commands import send_message, send_photo
from ny4twanty_proj.helpers import save_string


def handle_callback_queries(callback_data):
    callback_query = callback_data['callback_query']
    chat_id = callback_query['from']['id']
    data = callback_query['data']
    callback_id = callback_query['id']  # для answerCallbackQuery
    username = None
    first_name = None
    if "username" in callback_query['from']:
        username = callback_query['from']['username']
    if "first_name" in callback_query['from']:
        first_name = callback_query['from']['first_name']

    if 'back_to_' in data:
        print(data.split('_'))
        back_to = data.split('_')[2]

        try:
            slug = data.split('_')[3]
        except IndexError:
            slug = None
        try:
            sub_slug = data.split('_')[4]
        except IndexError:
            sub_slug = None
        try:
            code = data.split('_')[5]
        except IndexError:
            code = None

        if back_to == 'main':
            send_message(
                message=MAIN_MENU_TEXT.format(username=(username or first_name)),
                chat_id=chat_id,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            return "ok", 200
        elif back_to == 'catalog':
            send_message(
                message=CATALOG_TEXT.format(username=(username or first_name)),
                chat_id=chat_id,
                reply_markup=catalog_(back_to='main')
            )
            return "ok", 200
        elif back_to == 'category':
            if slug:
                send_photo(
                    photo='/home/valya/Pictures/telebot-e-shop/dress.jpg',
                    chat_id=chat_id,
                    caption=f'🔶Категорія:  _{save_string(slug)}_',
                    reply_markup=subcategory_markup(slug, back_to='catalog')
                )
            return "ok", 200
        elif back_to == 'subcategory':
            if sub_slug:
                send_photo(
                    photo='/home/valya/Pictures/telebot-e-shop/trousers-wide.jpg',
                    chat_id=chat_id,
                    caption=f'🔶Категорія:  _{save_string(slug)}_\n 🔶  Підкатегорія:  _{save_string(sub_slug)}_',
                    reply_markup=prod_list_markup(slug, sub_slug, back_to='category')
                )
            elif slug:
                send_photo(
                    photo='/home/valya/Pictures/telebot-e-shop/dress.jpg',
                    chat_id=chat_id,
                    caption=f'🔶Категорія:  _{save_string(slug)}_',
                    reply_markup=subcategory_markup(slug, back_to='catalog')
                )

            return "ok", 200

    if data == 'catalog':  # or data == 'back_to_catalog'
        send_message(
            message=CATALOG_TEXT.format(username=(username or first_name)),
            chat_id=chat_id,
            reply_markup=catalog_(back_to='main'),
        )
        return "ok", 200

    if "catalog_" in data:
        catalog = data.split('_')
        slug = catalog[-1]

        send_photo(
            photo='/home/valya/Pictures/telebot-e-shop/dress.jpg',
            chat_id=chat_id,
            caption=f'🔶Категорія:  _{save_string(slug)}_',
            reply_markup=subcategory_markup(slug, back_to='catalog')
        )

        return "ok", 200

    if "subcategory_" in data:
        sub_data = data.split('_')
        category = sub_data[1]
        subcategory = sub_data[2]

        send_photo(
            photo='/home/valya/Pictures/telebot-e-shop/trousers-wide.jpg',
            chat_id=chat_id,
            caption=f'🔶Категорія:  _{save_string(category)}_\n 🔶  Підкатегорія:  _{save_string(subcategory)}_',
            reply_markup=prod_list_markup(category, subcategory, back_to='category')
        )

        return "ok", 200

    if "product_" in data:
        sub_data = data.split('_')
        slug = sub_data[1]
        sub_slug = sub_data[2]
        code = sub_data[3]

        # print(save_string(sub_slug))
        send_photo(
            photo='/home/valya/Pictures/telebot-e-shop/my_moms_pants.jpg',
            chat_id=chat_id,
            caption=PROD_DETAIL_MESSAGE.format(
                category=save_string(slug),
                subcategory=save_string(sub_slug),
                title=save_string('Штани моєї мами'),
                code=save_string(code),
                description=save_string('Якийсь дуже довгий опис штанів моєї мами ...\n Капееееееец довгий'),
                price=f'${17}',
                measure=save_string(f'шт.')
            ),
            reply_markup=prod_detail_markup(slug=slug, sub_slug=sub_slug, code=code, quantity=14, back_to='subcategory')
        )

        return "ok", 200

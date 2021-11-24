from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    catalog_button = types.InlineKeyboardButton(text="📝 Каталог")
    cart_button = types.InlineKeyboardButton(text="🛒 Кошик")
    profile_button = types.InlineKeyboardButton(text="⚙️Профіль")

    keyboard.add(catalog_button).add(cart_button, profile_button)

    return keyboard


def main_menu():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text="📝 Каталог", callback_data='catalog'),
        types.InlineKeyboardButton(text="🛒 Кошик", callback_data='cart'),
        types.InlineKeyboardButton(text="⚙️Профіль", callback_data='profile')
    )

    return keyboard


def catalog_(back_to='main'):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text='Одяг', callback_data='catalog_dress'),
        types.InlineKeyboardButton(text='Продукти', callback_data='catalog_eat'),
    )
    keyboard.add(types.InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_{back_to}'))

    return keyboard


def subcategory_markup(slug, back_to='main'):
    keyboard = types.InlineKeyboardMarkup()
    subcategory_list = [
        ['Штани', 'trousers'],
        ['Куртки', 'jacket'],
        ['Футболки', 't-shirt'],
        ['Головні убори', 'headset']
    ]
    list_add = list()
    counter = 0

    for i, product in enumerate(subcategory_list):
        if counter > 1:
            counter = 0
            continue
        elif counter == 1:
            counter = 0

        if len(subcategory_list[i][0]) < 25 and len(subcategory_list[i + 1][0]) < 25:
            if i+1 != len(subcategory_list):
                list_add.append(
                    types.InlineKeyboardButton(text=f"{subcategory_list[i][0]}", callback_data=f'subcategory_{slug}_{subcategory_list[i][1]}')
                )
                list_add.append(
                    types.InlineKeyboardButton(text=f"{subcategory_list[i+1][0]}", callback_data=f'subcategory_{slug}_{subcategory_list[i+1][1]}')
                )

                keyboard.add(*list_add)
                counter += 2
                list_add = list()
            else:
                list_add.append(
                    types.InlineKeyboardButton(
                        text=f"{subcategory_list[i][0]}",
                        callback_data=f'product_{slug}_{subcategory_list[i][1]}'
                    )
                )

                keyboard.add(*list_add)
                counter += 1
                list_add = list()
        else:
            list_add.append(
                types.InlineKeyboardButton(
                    text=f"{subcategory_list[i][0]}",
                    callback_data=f'product_{slug}_{subcategory_list[i][1]}'
                )
            )

            keyboard.add(*list_add)
            counter += 1
            list_add = list()

    keyboard.add(types.InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_{back_to}_{slug}'))

    return keyboard


def prod_list_markup(slug, sub_slug, back_to='main'):
    keyboard = types.InlineKeyboardMarkup()
    product_list = [
        ['$16.5 Класичні штани', 'e00000001'],
        ['$20 Куртка La-Moda', 'e00000002'],
        ['$12 Футболка з V-вирізом', 'e00000003'],
        ['$1.59 Футболка Smailik', 'e00000004']
    ]
    list_add = list()
    counter = 0

    for i, product in enumerate(product_list):
        if counter > 1:
            counter = 0
            continue
        elif counter == 1:
            counter = 0

        if i+1 == len(product_list) or (len(product_list[i][0]) > 25):
            list_add.append(
                types.InlineKeyboardButton(
                    text=f"{product_list[i][0]}",
                    callback_data=f'product_{slug}_{sub_slug}_{product_list[i][1]}'
                )
            )

            keyboard.add(*list_add)
            counter += 1
            list_add = list()

            if i+1 == len(product_list):
                break
        elif i+1 != len(product_list):
            if len(product_list[i][0]) < 25 and len(product_list[i+1][0]) < 25:
                list_add.append(
                    types.InlineKeyboardButton(text=f"{product_list[i][0]}",
                                               callback_data=f'product_{slug}_{sub_slug}_{product_list[i][1]}')
                )
                list_add.append(
                    types.InlineKeyboardButton(text=f"{product_list[i + 1][0]}",
                                               callback_data=f'product_{slug}_{sub_slug}_{product_list[i + 1][1]}')
                )

                keyboard.add(*list_add)
                counter += 2
                list_add = list()
            else:
                list_add.append(
                    types.InlineKeyboardButton(
                        text=f"{product_list[i][0]}",
                        callback_data=f'product_{slug}_{sub_slug}_{product_list[i][1]}'
                    )
                )

                keyboard.add(*list_add)
                counter += 1
                list_add = list()

    keyboard.add(types.InlineKeyboardButton(text='⬅️ Назад', callback_data=f"back_to_{back_to}_{slug}_{sub_slug}"))

    return keyboard


def prod_detail_markup(slug, sub_slug, code, quantity, back_to='main'):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text='⬅️ Назад', callback_data=f"back_to_{back_to}_{slug}_{sub_slug}_{code}"),
        types.InlineKeyboardButton(text=f'В кошик ({quantity})', callback_data=f'add_{slug}_{sub_slug}_{code}')
    )
    keyboard.add(
        types.InlineKeyboardButton(text='Перейти в кошик', callback_data='to_cart'),
    )

    return keyboard


# CATALOG_KEYBOARD = catalog()
MAIN_KEYBOARD = main_keyboard()
MAIN_MENU_KEYBOARD = main_menu()
START_TEXT = """Привіт, {username}!\n\n🟢 Заходи в каталог та обирай товар."""

CATALOG_TEXT = """{username}, Ви в каталозі!\n\n🔶 Обирайте потрібну категорію\n🔶 В каталозі будуть карточки товарів з їхніми цінами та описом"""
MAIN_MENU_TEXT = """{username}, зараз Ви в головному меню. Якщо бажаєте продовжити ваші покупки, то оберіть одну з доступних опцій:\n\n"""
PROD_DETAIL_MESSAGE = """*Категорія:*  {category}\n*Підкатегорія:*  {subcategory}\n\n\n*Назва:* {title}\n*Артикул:* {code}\n*Опис:* {description}\n*Ціна:* {price} за {measure}"""


#

# end

# product_list = [
#     ['$16.5 Класичні штани', 'trousers'],
#     ['$20 Куртка La-Moda', 'jacket'],
#     ['$12.99 Футболка з V-вирізом lacoste і ще купа інформації', 't-shirt']
# ]
# list_add = list()
# counter = 0
#
# for i, product in enumerate(product_list):
#     if counter > 1:
#         counter = 0
#         continue
#     elif counter == 1:
#         counter = 0
#
#     if len(product_list[i][0]) < 25 and len(product_list[i + 1][0]) < 25:
#         if i+1 != len(product_list):
#             list_add.append(
#                 types.InlineKeyboardButton(text=f"{product_list[i][0]}", callback_data=f'product_{slug}_{product_list[i][1]}')
#             )
#             list_add.append(
#                 types.InlineKeyboardButton(text=f"{product_list[i+1][0]}", callback_data=f'product_{slug}_{product_list[i+1][1]}')
#             )
#
#             keyboard.add(*list_add)
#             counter += 2
#             list_add = list()
#         else:
#             list_add.append(
#                 types.InlineKeyboardButton(
#                     text=f"{product_list[i][0]}",
#                     callback_data=f'product_{slug}_{product_list[i][1]}'
#                 )
#             )
#
#             keyboard.add(*list_add)
#             counter += 1
#             list_add = list()
#     else:
#         list_add.append(
#             types.InlineKeyboardButton(
#                 text=f"{product_list[i][0]}",
#                 callback_data=f'product_{slug}_{product_list[i][1]}'
#             )
#         )
#
#         keyboard.add(*list_add)
#         counter += 1
#         list_add = list()

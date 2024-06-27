from telebot import TeleBot

from configs import TOKEN
from keyboards import *
from utils import *

bot = TeleBot(token=TOKEN)


# Декоратор - это то что меняет поведение функции
@bot.message_handler(commands=['start'])
def cmd_start(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Привет 🤖""")
    ask_user_name(message)


@bot.message_handler(commands=['help'])
def cmd_help(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Вы просили помощь ?😅
Я бот который знает 50 интересных рецептов блюд, напитков и десертов 📋
-----------------------------------------------------------------------
Вам всего лишь надо нажать на кнопку "Получить рецепт" и вы получите интересный рецепт 😄""")


@bot.message_handler(commands=['dev'])
def cmd_dev(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Интересно кто разработал этот бот ?👨🏻‍💻
Тогда вот вам контакты разработчика: 😊

https://t.me/azza_back_end_dev""")


def ask_user_name(message):
    chat_id = message.chat.id

    send_msg = bot.send_message(chat_id,
                                f"""Как к вам обращаться ?🤔""")

    bot.register_next_step_handler(send_msg, greeting_user)


def greeting_user(message):
    chat_id = message.chat.id
    name = message.text
    bot.send_message(chat_id,
                     f""" Привет {name} 👋🏻
Добро пожаловать в мир рецептов от
------------------ Willy Wonka 😉 ------------------
Чтобы получить рецепт нажми кнопку
--------------- Получить рецепт 📋 ---------------""",
                     reply_markup=generate_get_recipe_button())


@bot.message_handler(func=lambda message: message.text == "Получить рецепт 📋")
def send_recipe(message):
    chat_id = message.chat.id
    data = generate_normal_text()

    bot.send_photo(chat_id,
                   photo=data[1],
                   caption=data[0])



bot.polling(none_stop=True)

from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def generate_get_recipe_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    get_recipe_btn = KeyboardButton(text="Получить рецепт 📋")

    markup.add(get_recipe_btn)

    return markup

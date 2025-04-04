import json

import telebot
from telebot.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton

TOKEN = "5275596119:AAEuhyVOFr2yD6x6pUtVqqk3sn5FiZA3Is0"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo("https://imfamous1.github.io/mini_app/")
    button = KeyboardButton(text="Открыть Mini App", web_app=web_app)
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Запусти приложение по кнопке ниже:", reply_markup=keyboard)


@bot.message_handler(content_types=['web_app_data'])
def web_app_data_handler(message):
    data = json.loads(message.web_app_data.data)
    bot.send_message(message.from_user.id, f"Пользователь накликал: {data['value']}")
    print(f"Полученные данные с Mini App {data['value']}")


bot.polling()

import telebot
import config

bot = telebot.TeleBot("7793598131:AAHSv-wTY5gg57JUzYt5jktZ11N7yLdWVlg")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я работаю 24/7")

bot.polling(none_stop=True)
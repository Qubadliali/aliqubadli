import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 Твой токен
TOKEN = '8074984580:AAG45LhOCjxRbynmksTqez8HV8BQkX8279w'
bot = telebot.TeleBot(TOKEN)

# 🔗 Твоя ссылка
LINK = 'https://liget.ru/cheatsgames'

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("💣 Скачать чит на Standoff 2", url=LINK)
    btn2 = InlineKeyboardButton("🔥 Скачать чит на Brawl Stars", url=LINK)
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id, "Выбери игру для скачивания чита:", reply_markup=markup)

bot.polling()

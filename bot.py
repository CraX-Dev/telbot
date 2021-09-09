# mengimport package pyTelegramBotAPI
pip install pyTelegramBotAPI
import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('1516072532:AAF9hsylO3bknwo_llauZhAVLhNCXvoiIHQ')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo bro, ada apa?')

while True:
    try:
        bot.polling()
    except:
        pass

import telebot

bot = telebot.TeleBot('980131972:AAEH_Pg9-n3Sfnv-bSqUL_XypHE4rc30keE')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет пидрила')

bot.polling()

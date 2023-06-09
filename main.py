import telebot

token = "6163537042:AAGDTzM6pSbcXSQToZZTKzXLjsm7wn89CXc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'кукусик')

bot.polling(none_stop=True)
# ева топ ин ве ворлд
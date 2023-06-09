import telebot

token = "6163537042:AAGDTzM6pSbcXSQToZZTKzXLjsm7wn89CXc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'кукусик')

@bot.message_handler(content_types=["text"])
def return_message(message):
    if "дурак" in message.text.lower():
        bot.send_message(message.chat.id,'Сам дурак')
    elif "крутой" in message.text.lower():
        bot.send_message(message.chat.id, 'Да я такой')
    else:
        bot.send_message(message.chat.id,message.text + " -- это то что вы сказали")

bot.polling(none_stop=True)
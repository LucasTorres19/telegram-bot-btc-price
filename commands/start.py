import telebot

def _start(message,bot):
        
    msg = "hello! , you have woken me up now I will notify you of the price of bitcoin :D , use /help for more information."

    bot.send_message(message.chat.id,msg);


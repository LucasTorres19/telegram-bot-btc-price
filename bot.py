import os
import time
import requests
import schedule
from bs4 import BeautifulSoup  
from dotenv import load_dotenv

#cargar variables de entorno.
load_dotenv()

#iniciar el bot.
import telebot
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

users = []
users_timebtc = {}

#comandos.
@bot.message_handler(commands=['start'])
def _start(message):
    
    #verificar que el usuario no haya iniciado el bot.
    if(users.count(message.chat.id) == 0):

        users.append(message.chat.id)  #agregar el usuario al array de usuarios.
        
        welcome_msg = "hello! , you have woken me up now I will notify you of the price of bitcoin 😁, use /help for more information."
        bot.send_message(message.chat.id,welcome_msg)
        
        print("nuevo usuario con la id" + str(message.chat.id) + " inicio el bot.")

        start_bitcoin_msg = "To configure at what time you are notified of the price of btc use /timebtc , by default it is at 8:00 p.m. 😎"
        bot.send_message(message.chat.id,start_bitcoin_msg)

        #agregar al dicionario de horas.
        users_timebtc[message.chat.id] = "20:00"

    else:
        msg = "You have already started the operation for me 😏, to finish it use /end 😁"
        bot.send_message(message.chat.id,msg)

    #info
    print(users)
    print(users_timebtc)


@bot.message_handler(commands=['help'])
def _help(message):
    
    msg = "need help? 🤔, this is the list of commands:"
    msg1 = "start - this command starts the bot operation"
    msg2 = "end -end the use of the bot"
    
    bot.send_message(message.chat.id,msg)
    bot.send_message(message.chat.id,msg1)
    bot.send_message(message.chat.id,msg2)


@bot.message_handler(commands=['end'])
def _end(message):

    if(users.count(message.chat.id)!= 0):#si el usuario existe.

        #eliminar del array.
        users.remove(message.chat.id)

        goodbye_msg = "goodbye cowboy 🤠"
        bot.send_message(message.chat.id,goodbye_msg)

        print("usuario eliminado con la id:" +str(message.chat.id))

        print(users)#mostrar todos los usuarios.
    else:
        msg = "You have never started me 🤔, to do so use /start"
        bot.send_message(message.chat.id,msg)
    
#funciones auxiliares.
# def btc_scraping():
#     url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
#     soup = BeautifulSoup(url.content,'html.parser')
#     result = soup.find('td',{'class':'text-larger text-price'})
#     format_result = result.text

#     return format_result;

# def report():
#     btc_price_string =f'bitcoin price is {btc_scraping()}'
#     bot_sent_text(btc_price_string)

# def init_report(time):
#       schedule.every().day.at(time).do(report)


bot.infinity_polling()#while true de bot

# if __name__ == '__main__':
    
#     while True:
#         schedule.run_pending()
        
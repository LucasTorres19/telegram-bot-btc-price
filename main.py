import os
import requests
import schedule
from bs4 import BeautifulSoup  
from dotenv import load_dotenv


#cargar variables de entorno.
load_dotenv()

users = ["5425251939"]
bot_token= os.getenv('BOT_TOKEN')

def bot_capt_msj():

        url = "https://api.telegram.org/bot" + bot_token + "/getUpdates"
        response = requests.get(url)
    
        print(response.result)


def bot_sent_text(bot_message):

   
    bot_chatID= users[0]
    send_text =  'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content,'html.parser')
    result = soup.find('td',{'class':'text-larger text-price'})
    format_result = result.text

    return format_result;

def report():
    btc_price_string =f'El precio de Bitcoin es de {btc_scraping()}'
    bot_sent_text(btc_price_string)


if __name__ == '__main__':
    
    schedule.every().day.at("23:47").do(report)

    while True:
        schedule.run_pending()
        bot_capt_msj()
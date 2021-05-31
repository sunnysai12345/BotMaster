# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:36:36 2019
@author: saura
"""
import requests
import time
import schedule
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
def telegram_bot_sendtext(bot_message):
    bot_token='Your_Token'
    bot_chatID='your_chatid'
    send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response=requests.get(send_text)
    return response.json()
test=telegram_bot_sendtext("Testing bot")
print(test)
price=''
def getStock():
     bot_token='Your_Token'
     bot_chatID='your_chatid'
     response= "Let me fetch Latest quote ford you \n"
     symbol='ITC.NS'
     aapl=pdr.get_data_yahoo(symbol,  start=datetime.datetime(2019, 12, 14), 
                          end=datetime.datetime(2019, 12, 14))
     price=(aapl["Close"][0]).round(2)
     price=str(price)
     price="Current price for "+symbol+ " is "+price
     price=str(price.encode('utf-8','ignore'),errors='ignore')
     send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
     response=requests.get(send_text)
     print(response)
def btcTracker():
     bot_token='Your_Token'
     bot_chatID='your_chatid'
     response= "Let me fetch Latest quote for you \n"
     symbol='ETH-USD'
     aapl=pdr.get_data_yahoo(symbol,  start=datetime.datetime(2019, 12, 15), 
                          end=datetime.datetime(2019, 12, 15))
     price=(aapl["Close"][0]).round(2)
     price=str(price)
     price="Current price for "+symbol+ " is "+price
     price=str(price.encode('utf-8','ignore'),errors='ignore')
     send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
     response=requests.get(send_text)
     print(response)
import threading
while True:
    getStock()
    btcTracker()
    time.sleep(60)

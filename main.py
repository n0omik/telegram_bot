import json 
import requests 
from aiogram import Bot, Dispatcher, executor, types

key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
# running function to print btc crypto price
def currencies_price(currencies):
    currencies = ["BTCUSDT"] 
    url = key+currencies[j]   
    data = requests.get(url) 
    data = data.json() 
    return(f"{data['symbol']} price is {data['price']}") 

#API TOKEN for telegram bot n0omik
API_TOKEN = '6783402247:AAGLMtEeDpsKGgxY9PiT3BTxn-N4butoQ-k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#finction of start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет, я бот от Нумика, помогаю торговать на криптовалюте")

#finction of btc price
@dp.message_handler(commands=['Bitcoin_price'])
async def btc_price(message: types.Message):
   await message.reply(currencies_price)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime, date


pair = input('Pick the trading pair (for example: BTCUSDT): ')
timeframe = input('Enter timeframe (pick from 5m, 15m, 1h, 4h, 1d, 1w, 1M): ')
candles = input('How many candles you want to include (1000 max): ')
ma = input('Choose period for your MA (for example: 50): ')
tp = input('Choose take-profit percentage after which the order will be closed: ')
sl = input('Choose stop-loss percentage after which the order will be closed: ')

r = requests.post('https://paper-trader.frwd.one',
                  data={'pair': pair, 'timeframe': timeframe, 'candles': candles, 'ma': ma, 'tp': tp, 'sl': sl})
# Filling up form on site

soup = BeautifulSoup(r.text, 'html.parser').img
img_url = soup['src']  # Making source without html tag
img_full_url = img_url.replace('.', 'https://paper-trader.frwd.one', 1)  # making url to download pic

pic_name_date = date.today()
pic_name_time = datetime.now().time()

link = urllib.request.urlopen(img_full_url).read()  # Need to have byte-format to save pic
out = open(f"result_{pic_name_date}_{pic_name_time.hour}_{pic_name_time.minute}.jpg", "wb")  # Making normal name of pic
out.write(link)
out.close()
print('Операция прошлоа успешно! \nГрафик сохранён рядом с исполнительным файлом.')

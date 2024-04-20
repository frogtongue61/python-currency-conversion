import logging

#customlogger setup
logger = logging.getLogger("currency logger")

handler = logging.FileHandler('currency.log')
formatter = logging.Formatter('%(asctime)s '
                              '%(levelname)s'
                              '%(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('custom currency logger')


import requests

API_KEY = 'fca_live_JxudeyMEB5Qx9gs64HZhFXsmmloMegTXalD5n8CS'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['SEK','USD','CAD','GDP']

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = F"{BASE_URL}&base_currency = {base}%currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except Exception as e:
        print(e)
        return None

base = input('enter base currency (q for quit): ')

while True:

    data = convert_currency('USD')
    del data[base]

    for ticker,value in data.items():
        print(f'{ticker}: {value}')


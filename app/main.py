from config import token
from time import sleep
import requests

URL = 'https://api.telegram.org/bot'+token+'/'

def get_updates_json(request):  
    r = requests.get(request + 'getUpdates')
    return r.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    r = requests.post(URL+'sendMessage', json=params)
    return r.json()

def get_btc():
    r = requests.get('https://api.blockchain.info/stats').json()
    return r['market_price_usd']

def main():  
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
           send_message(get_chat_id(last_update(get_updates_json(URL))), get_btc())
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()
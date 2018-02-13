from config import token
import time
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

def get_btc(key):
    r = requests.get('https://api.blockchain.info/stats').json()
    return r[key]

def main():  
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
           datetime = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(int(str(get_btc('timestamp'))[:10])))
           marketprice = round(get_btc('market_price_usd'), 2)
           send_message(get_chat_id(last_update(get_updates_json(URL))), "По состоянию на {0} курс Биткоина равен {1} USD".format(datetime, marketprice))
           update_id += 1
        time.sleep(1)       

if __name__ == '__main__':  
    main()
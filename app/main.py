#from flask import flask
from config import token
import requests
import json

URL = 'https://api.telegram.org/bot'+token+'/'

def write_json(data, filename='answer.json'):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_updates():
    r = requests.get(URL+'getUpdates')
    return r.json()

def send_message(chat_id, text="blank text"):
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(URL+'sendMessage', json=answer)
    return r.json()

#method could be getUpdates
def main():
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    send_message(chat_id)

#app = Flask(__name__)

#if __name__ is '__main__':
#    app.run()
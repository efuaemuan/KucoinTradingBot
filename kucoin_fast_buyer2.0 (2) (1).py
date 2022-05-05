import asyncio
import threading
import time
import datetime
import requests
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient
from config import *
import math
import datetime
import json

from kukoin import my_kukoin_handler

kukoin_prices = {}
# Kukoin update prices
symbols = {}

track = {}

def read_json():
    global track
    try:
        with open('coins_tracker.json', 'r') as fl:
            hist = fl.read()
            hist = json.loads(hist)
            track = hist
    except Exception as e:
        print("Error opening historiy listing file", e)
        return False

def refresh_the_json_write():
    global track
    try:
        with open('coins_tracker.json', 'w') as fl:
            # print('here is hist', hist)
            json.dump(track, fl)
    except:
        print("Error opening historiy listing file")
        return False

print("Starting the code ")
read_json()
print("The code is running ... ")

c=0
async def run_ws(args):
    global kukoin_prices ,tst ,c

    async def deal_msg(msg):
        global c,tst, symbols, track
        kukoin_prices[msg['subject']] = msg['data']['price']
        #print(msg)
        #print(msg['subject'].strip("-USDT").upper(), symbols)
        if '-' not in msg['subject'].replace("-USDT",''):
            tt = msg['subject'].replace("-USDT",'USDT').upper()
            if tt in list_of_coins and tt not in track.keys():
                print("Buying   ",tt)
                track[tt] = float(msg['data']['price'])
                print("price:",track[tt])
                my_hand = my_kukoin_handler(key=kukoin_key,sec=kukoin_secret,pas=kukoin_passphrase)
                #qtt =round(unit_investement/float(msg['data']['price']),3)
                my_hand.buy(coin_no_usdt=msg['subject'],qty=0,price=msg['data']['price'])
                refresh_the_json_write()
                print("bought")
            elif  tt  in track.keys() and not track[tt] == -1 and  float(msg['data']['price'])>(1+take_profit)*track[tt]:
                track[tt] = -1
                refresh_the_json_write()
                print("Selling  ", tt)
            #if tt in  symbols or tt in track.keys() :


    client = WsToken()
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    await ws_client.subscribe('/market/ticker:all')
    while True:
        await asyncio.sleep(60)


def update_the_prices(args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_ws(args))
    loop.close()


update_the_prices('text')






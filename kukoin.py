
from kucoin.client import Trade, Market, User
from config import *

class my_kukoin_handler:
    def __init__(self,key=kukoin_key,sec=kukoin_secret,pas=kukoin_passphrase):
        self.api_key = key
        self.api_secret = sec
        self.api_passphrase = pas
        self.client = Trade(key=self.api_key, secret=self.api_secret, passphrase=self.api_passphrase, is_sandbox=False, url='')
        self.user = User(key=self.api_key, secret=self.api_secret, passphrase=self.api_passphrase)
        #print(self.user.get_account(accountId=''))
        #print(self.user.get_account(accountId='')) #61e4749064d1460001b3130b
        #input('here')
    def get_balance(self):
        to_Return= 0
        for elt in self.user.get_account(accountId=''):
            if elt['currency'] == "USDT":
                to_Return = float(elt['balance'])
        return to_Return

    def update_client(self):
        self.client = Trade(key=self.api_key, secret=self.api_secret, passphrase=self.api_passphrase, is_sandbox=False,url='')

    def buy(self,coin_no_usdt,qty,price):
        try:
            money =  self.get_balance()
            tn = len(str(price).split()[1])
            qty =round(money / price, 3)
            order_id = self.client.create_market_order(str(coin_no_usdt).upper().strip(), 'buy', size=str(qty))
            print(order_id)
        except Exception as e :
            print('Kukoin error while buyin has occured',str(e))

def get_kukoin_pairs():
    client = Market(url='https://api.kucoin.com')
    lst = {}
    for elt in client.get_symbol_list():
        if 'USDT' in elt['symbol'] or 'BTC' in elt['symbol']:
            lst[elt['symbol']] = 0
    return lst

tst  = my_kukoin_handler()
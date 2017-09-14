#!/usr/bin/env python

#enter your keys here
api_key = 'REDACTED'
api_secret = 'REDACTED'

from binance.client import Client
client = Client(api_key, api_secret)

time_res = client.get_server_time()

# Working examples

# orders = client.get_all_orders(symbol='BNBBTC', limit=10)
# print(orders)

# tickers = client.get_all_tickers()
# print(tickers)

# Not working below:
# openorders = client.get_open_orders()
# print(openorders)

RECV_WINDOW=6000000

class Monitor:
    def __init__(self):
        self.bac = Client(api_key,api_secret)
    def my_balance(self):
        print(self.bac.get_account(recvWindow=RECV_WINDOW))


m = Monitor()
m.my_balance()
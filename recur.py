import pdb
from robin_stocks import *
import robin_stocks.robinhood as r
import time
import os
import sys

os.system("clear")
login = r.login(YOUR_USERNAME,YOUR_PASSWORD)

TICKER = sys.argv[1]
# Dollars
INVESTMENT = 1
# Seconds in a Day
DELAY = 86400

while True:
    for i in range(DELAY):
        print (f"Order placed for {TICKER}")
        print(f"Coutdown: {DELAY - i}")
        time.sleep(1)
        os.system("clear")
    r.order_buy_market(TICKER, INVESTMENT)
    time.sleep(DELAY)

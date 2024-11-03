import pdb
from robin_stocks import *
import robin_stocks.robinhood as r
import time
import os
import sys

os.system("clear")


TICKER = sys.argv[1]
SELLS = sys.argv[2]

login = r.login(YOUR_USERNAME,YOUR_PASSWORD)

prev_count = None
while True:
    events = r.get_events(TICKER)
    count = 0
    os.system("clear")
    print(f"{TICKER} Total Options Exercise(s): {len(events)}")

    for event in events:
        # print("type" in event)
        if (event["type"] == "assignment"):
            count += 1
    if prev_count != count and prev_count != None:
        print("Assignement: SELL SELL SELL")
        for sell in SELLS:
            r.order_sell_market(TICKER, 100 * SELLS)
        input("We have put in our orders. Now we wait.... Press Enter to End Trading for the Day")
        sys.exit(1)

    prev_count = count
    time.sleep(1)

# count_state = {} 
    # while True:
    #     for ticker in LONG_NOTPOSSIBLE:
    #         events = r.get_events(ticker)
    #         event_count = len(events)
    #         log(f"Exercise Event Count: {event_count}")
    #         if ticker in count_state and count_state[ticker] != event_count:
    #             set(exercise_flag, True)
    #             log(f"{ticker} has new events")
    #         count_state[ticker] = event_count
    #         # for event in events:
    #         #     print("option" in event)
    #     log(count_state)
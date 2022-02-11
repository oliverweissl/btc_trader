import asyncio, websockets, json
import pandas as pd

from ta.utils import dropna
from ta.trend import ema_indicator as Ema
from ta.momentum import StochRSIIndicator as Srsi
from ta.volatility import AverageTrueRange as Atr

import websocket, pprint, numpy
import config
from termcolor import colored
#from binance.client import Client
#from binance.enums import *

#Trade data
TICKER = "BTCUSDT"
TIME_FRAME = "3m"
TRADE_SIZE = 0.05 #trades in percentage size of available funds
SOCKET = f"wss://stream.binance.com:9443/ws/{TICKER.lower()}@kline_{TIME_FRAME}"

#EMA Settings
FAST_EMA = 8
MEDIUM_EMA = 14
SLOW_EMA = 50

#Stochastic RSI
K = 3 #stochastic fast
D = 3 #signal line
RSI_LEN = 14
STC_LEN = 14 #stochastic length
UPPER_BAND = 50
LOWER_BAND = 50

#ATR settings
ATR_LEN = 14


#client = Client(config.API_KEY, config.API_SECRET, tld='us')

#assets = client.get_asset_balance(asset='USDT')
#trade_amount = assets * TRADE_SIZE
open_position = False
closes = []
high = []
low = []

#Indicators
fast_EMA = Ema(closes, window=FAST_EMA, fillna=False)
medium_EMA = Ema(closes, window=MEDIUM_EMA_EMA, fillna=False)
slow_EMA = Ema(closes, window=SLOW_EMA_EMA, fillna=False)

stochastic_rsi = Srsi(closes, window=RSI_LEN, smooth1=D, smooth2=K, fillna=False)

atr = Atr(high,low, closes, window=ATR_LEN, fillna=False)

#def order():

def open(ws):
    print(colored("Opened Position", "grey"))
def stop_loss(ws):
    print(colored("Triggered Stop-Loss","red"))
def take_profit(ws):
    print(colored("Took Profit!", "green"))


#ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
#ws.run_forever()

def clean_df(data):
    ddata = pd.json_normalize(data)
    df = ddata.loc[:, ["s","E","k.c","k.h","k.l"]]
    df.columns = ["Symbol", "Time", "ClosingPrice", "High", "Low"]
    df.ClosingPrice = df.ClosingPrice.astype(float)
    df.Time = pd.to_datetime(df.Time, unit="ms")
    return df

async def main():
    stream = websockets.connect(SOCKET)
    async with stream as reciever:
        data = await reciever.recv()
        parsed_data = json.loads(data)
        df = clean_df(parsed_data)
        print(df)

if __name__ == '__main__':
    #test_data = {"e":"kline","E":1644603765123,"s":"BTCUSDT","k":{"t":1644603720000,"T":1644603779999,"s":"BTCUSDT","i":"1m","f":1254825619,"L":1254825905,"o":"43446.31000000","c":"43452.98000000","h":"43471.80000000","l":"43445.65000000","v":"8.79368000","n":287,"x":"false","q":"382184.60369420","V":"6.08964000","Q":"264652.67491080","B":"0"}}
    #print(clean_df(test_data))

    asyncio.run(main())

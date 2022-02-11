import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *

#Trade data
SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
TICKER = "BTCUSD"

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
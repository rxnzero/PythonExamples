import talib
import pandas as pd
import pyupbit

df = pyupbit.get_ohlcv("KRW-ETH", count=100)

close = df['close'].values
print(close)

upperband, middleband, lowerband = talib.BBANDS(
    close, 20, 2, 2)

print(upperband)
print(middleband)
print(lowerband)
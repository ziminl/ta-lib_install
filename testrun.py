import numpy as np
import pandas as pd
import talib

data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'close': [100, 102, 105, 107, 106, 108, 110, 112, 115, 118]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

sma = talib.SMA(df['close'].values.astype('float64'), timeperiod=5)
df['SMA'] = sma

macd, macdsignal, macdhist = talib.MACD(df['close'].values.astype('float64'), fastperiod=12, slowperiod=26, signalperiod=9)
df['MACD'] = macd
df['MACD_Signal'] = macdsignal
df['MACD_Hist'] = macdhist

print("\nData with SMA and MACD:")
print(df)

print("\nSMA Values:")
print(df['SMA'])
print("\nMACD Values:")
print(df['MACD'])

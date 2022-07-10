from binance.client import Client
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

key = "yy6YUWGLpkwZKdkxie6XCpLYAAEnkTm3ab27fbPcT5VtwQAXZFu1iDglGKA2bUak"
secret = "s5nvlXixNMECEfSEp4eX4wU7uv1nKVfG1iXGmk84EdjfwhQOb3jtL6Y8wdgF46Kj"
client = Client(key, secret)

fxpair = input("Please enter crypto trading pair without slash all uppercase: "  )
#interval = input("Please enter time interval: "  )
kline = client.get_historical_klines(fxpair, Client.KLINE_INTERVAL_30MINUTE,"1 Jan, 2021")
df = pd.DataFrame(kline)
df.columns = ["Open Time","Open","High","Low", "Close", "Volume", "Close Time", "Quote Asset Volume","Number of trades", "TB Base Volume", "TB Quote Volume", "Ignore"]
df = df.drop('Ignore', 1)
df["Open Time"]=pd.to_datetime(df["Open Time"]/1000,unit="s")
df["Close Time"]=pd.to_datetime(df["Close Time"]/1000,unit="s")
numeric_columns = ["Open","High","Low", "Close", "Volume","Quote Asset Volume","TB Base Volume", "TB Quote Volume"]
df[numeric_columns]=df[numeric_columns].apply(pd.to_numeric,axis=1)

df["Year"] = df["Open Time"].dt.year
df["Month"] = df["Open Time"].dt.month
df["Day"] = df["Open Time"].dt.day
df["Hour"] = df["Open Time"].dt.hour
df["Minute"] = df["Open Time"].dt.minute
df["Second"] = df["Open Time"].dt.second
#df.set_index("Open Time",inplace=True)
print(df.head())

sns.lineplot(x="Open Time",y="Close",data=df)
plt.show()

#df.set_index("Open Time",inplace=True)






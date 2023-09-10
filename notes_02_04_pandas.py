# -*- coding: utf-8 -*-
"""NOTES 02.04 - PANDAS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rramosp/ai4eng.v1/blob/main/content/NOTES%2002.04%20-%20PANDAS.ipynb

# 02.04 - PANDAS
"""

!wget --no-cache -O init.py -q https://raw.githubusercontent.com/rramosp/ai4eng.v1/main/content/init.py
import init; init.init(force_download=False); init.get_weblink()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

"""## `pandas` is mostly about manipulating tables of data

see this cheat sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

"""



"""## Pandas main object is a `DataFrame`

- can read .csv, .excel, etc.

"""

!head local/data/internet_facebook.dat

!wc local/data/weather_data_austin_2010.csv

df = pd.read_csv('local/data/internet_facebook.dat', index_col='# Pais')
df

df.head()

df.tail()

df.columns

df.index

"""**fix the index name**"""

df.index.name="Pais"
df.head()

df.describe()

df.info()



"""**a dataframe is made of `Series`**. Observe that each series has **its own type**"""

s1 = df["Uso_Internet"]
type(s1)

s1



"""if the column name is not too fancy (empy spaces, accents, etc.) we can use columns names as python syntax."""

df.Uso_Facebook

"""## DataFrame indexing

is **NOT** exactly like numpy

- first index
    - if string refers to columns
    - if `Series` of booleans is used as a filter
    
- for selecting columns:
    - use `.loc` to select by Index
    - use `.iloc` to select by position   
"""

df["Colombia"]

df.loc["Colombia"]

"""Index semantics is exact!!"""

df.loc["Colombia":"Spain"]

df.iloc[10:15]

"""filtering"""

df[df.Uso_Internet>80]

"""combined conditions"""

df[(df.Uso_Internet>50)&(df.Uso_Facebook>50)]

df[(df.Uso_Internet>50)|(df.Uso_Facebook>50)]

"""## Managing data

observe csv structure:
- missing column name
- missing data
"""

!head local/data/comptagevelo2009.csv

d = pd.read_csv("local/data/comptagevelo2009.csv")
d

d.columns, d.shape

"""numerical features"""

d.describe()

d["Berri1"].head()

d["Unnamed: 1"].unique()

d["Berri1"].unique()

d["Berri1"].dtype, d["Date"].dtype, d["Unnamed: 1"].dtype

d.index

"""## Fixing data

observe we set one column as the index one, and we **convert** it to date object type
"""

d.Date

d.index = pd.to_datetime(d.Date)
del(d["Date"])
del(d["Unnamed: 1"])
d.head()

d.index



"""let's fix columns names"""

d.columns=["Berri", "Mneuve1", "Mneuve2", "Brebeuf"]
d.head()

for col in d.columns:
    print (col, np.sum(pd.isnull(d[col])))

d.shape

d['Brebeuf'].describe()

plt.hist(d.Brebeuf, bins=30);

"""**fix missing**!!!"""

d.Brebeuf.fillna(d.Brebeuf.mean(), inplace=True)

d['Brebeuf'].describe()

plt.hist(d.Brebeuf, bins=30);

d

"""let's make sure it is sorted"""

d.sort_index(inplace=True)
d.head()

"""## Filtering"""

d[d.Berri>6000]

d[(d.Berri>6000) & (d.Brebeuf<7000)]

"""## Locating"""

d[d.Berri>5500].sort_index(axis=0)

d.iloc[100:110]

"""**dates as INDEX have special semantics**"""

d.loc["2009-10-01":"2009-10-10"]

"""can do sorting across any criteria"""

d.sort_values(by="Berri").head()

"""and chain operations"""

d.sort_values(by="Berri").loc["2009-10-01":"2009-10-10"]

"""## Time series operations"""

d.rolling(3).mean().head(10)

d.index = d.index + pd.Timedelta("5m")
d.head()

d.shift(freq=pd.Timedelta(days=365)).head()

"""## Downsampling"""

d.resample(pd.Timedelta("2d")).first().head()

d.resample(pd.Timedelta("2d")).mean().head()

"""## Upsampling"""

d.resample(pd.Timedelta("12h")).first().head()

d.resample(pd.Timedelta("12h")).fillna(method="pad").head()

"""## Building Dataframes from other structures"""

a = np.random.randint(10,size=(20,5))
a

k = pd.DataFrame(a, columns=["uno", "dos", "tres", "cuatro", "cinco"], index=range(10,10+len(a)))
k

"""## `.values` access the underlying `numpy` structure"""

d.values

"""## some out-of-the-box plotting

but recall that we always can do custom plotting
"""

d.plot(figsize=(15,3))

plt.figure(figsize=(15,3))
plt.plot(d.Berri)

d.Berri.cumsum().plot()

plt.scatter(d.Berri, d.Brebeuf)

pd.plotting.scatter_matrix(d, figsize=(10,10));

"""## Grouping"""

d["month"] = [i.month for i in d.index]
d.head()

d.groupby("month").max()

d.groupby("month").count()

"""## Time series

observe we can **establish at load time** many thing if the dataset is relatively clean
"""

tiempo=pd.read_csv('local/data/weather_data_austin_2010.csv',parse_dates=['Date'], dayfirst=True ,index_col='Date')
tiempo

tiempo.loc['2010-08-01':'2010-10-30']

tiempo.loc['2010-06'].head()

tiempo.sample(10)

tiempo.sample(frac=0.01)

"""## Resampling"""

tiempo.head()

tiempo.resample("5d").mean().head()

tiempo.resample("5d").mean().head()

tiempo.resample("5d").mean().head()

tiempo.resample("30min").mean()[:15]

subt=tiempo.between_time(start_time='1:00',end_time='12:00')
subt

tiempo.index.weekday

tiempo.index.month

tiempo.index.day

tiempo.plot(style='.')

tiempo['2010-01'].plot()

tiempo['2010-01-04'].plot()

"""## Rolling operations"""

import pandas as pd
### permite obtener data frames directamente de internet
!pip install yfinance

import yfinance as yf



#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
gs = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#see your data
gs

gs.Close.rolling(10).mean().head(20)

plt.figure(figsize=(20,3))
plt.plot(gs.Close)
plt.plot(gs.Close.rolling(50).mean())

plt.figure(figsize=(20,3))
plt.plot(gs.iloc[:400].Close, label="original")
plt.plot(gs.iloc[:400].Close.rolling(50).mean(), label="rolling")
plt.plot(gs.iloc[:400].Close.rolling(50, center=True).mean(), label="center")
plt.legend();

plt.figure(figsize=(20,3))
plt.plot(gs.iloc[:400].Close.rolling(10).mean())

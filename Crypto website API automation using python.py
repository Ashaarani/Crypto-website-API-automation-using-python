#!/usr/bin/env python
# coding: utf-8

# In[91]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd


# In[92]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
       'start':'1',
       'limit':'15',
       'convert':'USD'
    }
    headers = {
       'Accepts': 'application/json',
       'X-CMC_PRO_API_KEY': '9f13ea63-dc84-4e3d-890b-6c7f27a100ca',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    
    df2= pd.json_normalize(data['data'])
    df2['timestamp']= pd.to_datetime('now')
    
    if df.empty:
        df = df2
    else:
        df = pd.concat([df, df2], ignore_index=True)
    
print(df)


    


# In[93]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[94]:


# to convert the scientific notation
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[95]:


df


# In[97]:


#Coin trends over time
df1= df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3=df1.stack()
df3


# In[98]:


type(df3)


# In[99]:


df4=df3.to_frame(name='values')
df4


# In[100]:


df4.count()


# In[101]:


df5=df4.reset_index()
df5


# In[102]:


df6=df5.rename(columns={'level_1':'Percentage_Change'})
df6


# In[103]:


df6['Percentage_Change']= df6['Percentage_Change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df6


# In[104]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[106]:


sns.catplot(x='Percentage_Change',y='values',hue='name', data = df6, kind='point')


# In[115]:


df6= df[['name','quote.USD.price','timestamp']]
df6 = df6[df6['name'].isin(['Bitcoin', 'Ethereum'])]
df6


# In[116]:


sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp',y='quote.USD.price',hue='name',data=df6)
plt.title('Price Comparison of Bitcoin and Ethereum Over Time')
plt.legend(title='Cryptocurrency')
plt.grid(True)


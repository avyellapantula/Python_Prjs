# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df_sales = pd.read_csv('data\sales_train_clean.csv')

# df2 = df.rename({'a': 'X', 'b': 'Y'}, axis='columns')

df_sales = df_sales.rename({'Unnamed: 0':'date'}, axis='columns')

# time to plot
fig = px.line(df_sales, x='date', y='agg_sum')
fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)
fig.show()


df_sales.plot(kind='line',
              x='date',
              y='agg_sum',
              figsize=(15, 5))


sales=pd.read_csv('data\sales_train_validation.csv')
sell=pd.read_csv('data\sell_prices.csv')
cal=pd.read_csv('data\calendar.csv')
cal['date']=pd.to_datetime(cal['date'])


cal_events=cal.dropna()

ca_snaps=cal[(cal['snap_TX'] == 0) & (cal['snap_WI'] == 0) & (cal['snap_CA'] == 1)]
tx_snaps=cal[(cal['snap_CA'] == 0) & (cal['snap_WI'] == 0) & (cal['snap_TX'] == 1)]
wi_snaps=cal[(cal['snap_TX'] == 0) & (cal['snap_CA'] == 0) & (cal['snap_WI'] == 1)]
all_snaps=cal[(cal != 0).all(1)]


# id 	item_id 	dept_id 	cat_id 	store_id 	state_id


df = sales.copy()

df.loc[len(df)] = sums

df_t=df.transpose()
df_t = df_t.drop(['item_id','dept_id','cat_id','store_id','state_id'])

new_header = df_t.iloc[0] #grab the first row for the header
df_t = df_t[1:] #take the data less the header row
df_t.columns = new_header #set the header row as the df header

# change position of columns
cols=df_t.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_t=df_t[cols]

df_t=df_t.reset_index()
df_t= df_t.rename({'index':'d_num'}, axis='columns')

agg_sums=df_t[['ttl_items']].copy()
agg_sums['year']=cal['year']
agg_sums['month']=cal['month']

print(agg_sums.head())

# ex_sum = ex.groupby(['foo','bar']).sum()
aggs = agg_sums.groupby(['year', 'month']).sum()

print(aggs.head())

aggs_piv = aggs.pivot('year', 'month', 'ttl_items')
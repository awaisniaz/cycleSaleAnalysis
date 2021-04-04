import pandas as pd

data = pd.read_csv('FremontBridge.csv', index_col='Date')
print(data.head(5))
data.columns = ['East', 'West']
data['Total'] = data['East'] + data['West']
print(data.describe())
print(data.info())

# Visualization of data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data.plot()
plt.xlabel('West')
plt.ylabel('East')
plt.show()

# weekly = data.resample('W').sum()
# weekly.plot(style =[':','--','-'])
# plt.ylabel('weekly bycycle count')
# plt.show()

# daily = data.resample('D').sum()
# daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
# plt.ylabel('mean hourly count')
# plt.show()


import numpy as np
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks= hourly_ticks, style=[':', '--', '-'])
plt.ylabel("Traffic according to time")
plt.show()

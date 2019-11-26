#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pyplot import figure

data = pd.read_csv("C:/Users/DELL/Downloads/ethusd_tweets.csv")

print(data.head())

ax=plt.gca()

data.plot(kind='line',x='Date',y='Open',ax=ax)
data.plot(kind='line',x='Date',y='Close',ax=ax)
data.plot(kind='line',x='Date',y='High',ax=ax)
data.plot(kind='line',x='Date',y='Low',ax=ax)

figure(num=None, figsize=(100,100), dpi=1600)
plt.show()




# In[ ]:





# In[ ]:





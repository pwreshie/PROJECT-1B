#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import csv
from datetime import datetime


# In[7]:


s = []
for i in range(1, 13):
    s.append(datetime(2020, i, 1).strftime('%B'))

list_of_files = []


for i in s:
    list_of_files.append(f'/Users/User/Downloads/Sales_Data/Sales_{i}_2019.csv')


# In[53]:


s


# In[54]:


list_of_files


# In[55]:


data.shape


# In[56]:


data = pd.read_csv(list_of_files[0])


# In[57]:


data


# In[58]:


data1 = pd.read_csv(list_of_files[1])


# In[59]:


data1


# In[60]:


data2 = pd.read_csv(list_of_files[2])


# In[61]:


data2


# In[62]:


data = []
for file in list_of_files:
    data.append(pd.read_csv(file))


# In[ ]:





# In[63]:


##PEAK PERIOD


# In[64]:


data = pd.concat(data, ignore_index=True)


# In[65]:


data['Purchase Address'][186000].split(',')[1].strip()


# In[66]:


def convert_state(data):
    if isinstance(data, float):
        return 'n/a'
    else:
        return data.split(',')[1].strip(' ')


# In[67]:


# d = 0
# for i in list(data['Purchase Address']):
#     if isinstance(i, float):
#         print('stuff', i)
#         d += 1


# In[68]:


data['State'] = data['Purchase Address'].apply(parse_address)


# In[69]:


pd.DataFrame(data['State']).head(10)


# In[70]:


data['Time'] = data['Order Date'].apply(parse_date)


# In[71]:


data['Time']


# In[72]:


d = map(convert_state, list(data['Purchase Address']))


# In[73]:


def parse_address(value, *, default=None):
    try:
        clean = value.split(',')[2][1:3]
        if not clean:
            return default
        else:
            return clean
    except Exception:
        return default


# In[74]:


def parse_date(value, *, fmt='%m/%d/%y %H:%M', default=None):
    try:
        return datetime.strptime(value, fmt)
    except Exception:
        return default


# In[75]:


isinstance(2.3, float)


# In[76]:


def parse_int(value, *, default=None):
    try:
        return int(value)
    except Exception:
        return default


# In[77]:


def parse_float(value, *, default=None):
    try:
        return float(value)
    except Exception:
        return default


# In[78]:


data['Quantity Ordered_int'] = data['Quantity Ordered'].apply(parse_int)


# In[79]:


data['Price Each_int'] = data['Price Each'].apply(parse_float)


# In[80]:


data['Total Value'] = data['Quantity Ordered_int'] * data['Price Each_int']


# In[81]:


data['Total Value']


# In[82]:


data


# In[ ]:





# In[83]:


##STATE WITH MOST IMPACT


# In[84]:


state_impact = pd.DataFrame(data.groupby("State")["Total Value"].sum()).reset_index()
state_impact


# In[85]:


state_impact.sort_values(by = "Total Value", inplace = True, ascending=False)


# In[86]:


# state_impact['Total Value'].plot(x=state_impact['State'], y=state_impact['Total Value'])


# In[87]:


state_impact['Total Value'] = state_impact['Total Value'].apply(lambda x: int(x))


# In[88]:


state_impact


# In[89]:


##LINE PLOT


# In[90]:


plt.plot(state_impact['State'], state_impact['Total Value'],linewidth = 3, color = "blue", alpha = 0.7)

plt.title("State Impact by Time")
plt.xlabel("State")
plt.ylabel("Total Value")

plt.show()
# plt.plot


# In[91]:


##BAR CHART


# In[92]:


all_colors = ["blue", "pink", "orange", "green", "cyan", "purple", "brown", "yellow", "brown", "indigo", "grey"]


# In[93]:


plt.bar(state_impact['State'], state_impact['Total Value'], width = 0.7, color = all_colors[:  11])


plt.title("State Impact by Time")
plt.xlabel("State")
plt.ylabel("Total Value")

plt.show()


# In[ ]:





# In[94]:


##PIE CHART


# In[95]:


plt.pie(state_impact["Total Value"], labels = state_impact["State"], radius = 2.0, autopct = "%0.2f%%", explode = [0.1,0,0,0,0,0,0,0])

plt.show()


# In[ ]:





# In[ ]:





# In[96]:


##CHI SQUARE


# In[97]:


from scipy.stats import chi2_contingency as chi


# In[98]:


chi(pd.crosstab(state_impact["State"], state_impact["Total Value"]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





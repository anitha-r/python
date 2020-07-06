#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import pearsonr, spearmanr


# In[11]:


transit = pd.read_csv("Transit_System_Time_Series.csv")
transit.head()


# In[12]:


transit.info()


# In[14]:


#convert values in the date column to a datetime data type
transit['Fiscal Year End Date'] = pd.DatetimeIndex(transit['Fiscal Year End Date'])
transit['Fiscal Year End Date'].head()


# In[21]:



np.corrcoef(transit['Total Employee Count'], transit['Total Hours Worked'])


# In[22]:


np.corrcoef(transit['Total Actual Vehicle/Passenger Car Revenue Hours'], transit['Total Train Revenue Hours'])


# In[23]:


transit['Total Actual Vehicle/Passenger Car Revenue Hours'].corr(transit['Total Train Revenue Hours'])


# In[24]:


#calculate linear relationship between two values - Pearsonr correlation coefficient
#returns correlation coefficient and 2-tailed p-value
#p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Pearson correlation
#at least as extreme as the one computed from these datasets
pearsonr(transit['Total Actual Vehicle/Passenger Car Revenue Hours'], transit['Total Train Revenue Hours'])


# In[27]:


##since "array must not contain nans", remove the nan values in both columns
x,y= transit['Total Actual Vehicle/Passenger Car Revenue Hours'], transit['Total Train Revenue Hours']
nas=np.logical_or(np.isnan(x), np.isnan(y))
corr = pearsonr(x[~nas], y[~nas])
corr


# In[29]:


#calculate a Spearman correlation coefficient with associated p-value
#the rank-order correlation coefficient is a non-parametric measure of the monotonicity of the relationship between 2 datasets
#does not assume both the datasets are normally distributed
spearmanr(x[~nas], y[~nas])


# In[32]:


#visualize the correlation
plt.figure(figsize=(10,8))
plt.scatter(transit['Total Actual Vehicle/Passenger Car Revenue Hours'], transit['Total Train Revenue Hours'],color='m')
plt.title('Total Revenue hours')
plt.xlabel('Total Actual Vehicle/Passenger Car Revenue Hours')
plt.ylabel('Total Train Revenue Hours')

plt.show()


# In[39]:


plt.figure(figsize=(10,8))
plt.scatter(transit['Maintenance facilities Less than 200 vehicles'], transit['Total Maintenance Facilities'],color='m')
#plt.title('Total Revenue hours')
#plt.xlabel('Total Actual Vehicle/Passenger Car Revenue Hours')
#plt.ylabel('Total Train Revenue Hours')

plt.show()


# In[50]:


#transit.filter(regex="facilities.*")
plt.figure(figsize=(10,8))
plt.scatter(transit['Total Current Assets'], transit['Inventory (1130)'],color='g')
#plt.title('current assets vs investment')
#plt.xlabel('Total Current Assets')
#plt.ylabel('Investments')

plt.show()


# In[49]:


transit.filter(regex="Inventory.*")


# In[54]:


#calculate correlation between all pairs of variables in the data
corr1 = transit.corr()
corr1.to_csv("corrfile.csv")


# In[55]:


#generate heat map
plt.figure(figsize=(10,8))
plt.matshow(corr1, fignum=False, aspect='equal')
columns = len(transit.columns)

plt.xticks(range(columns), transit.columns)
plt.yticks(range(columns), transit.columns)
plt.colorbar()
plt.xticks(rotation=90)
plt.title('Correlations', y=1.2)

plt.show()


# In[ ]:





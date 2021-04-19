#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


df= pd.read_csv('NOAA_GlobalSummary_Day.csv')
df.tail(25)


# In[24]:


#TEMP - Mean temperature (.1 Fahrenheit)
#DEWP - Mean dew point (.1 Fahrenheit)
#SLP - Mean sea level pressure (.1 mb)
#STP - Mean station pressure (.1 mb)
#VISIB - Mean visibility (.1 miles)
#WDSP – Mean wind speed (.1 knots)
#MXSPD - Maximum sustained wind speed (.1 knots)
#GUST - Maximum wind gust (.1 knots)
#MAX - Maximum temperature (.1 Fahrenheit)
#MIN - Minimum temperature (.1 Fahrenheit)
#PRCP - Precipitation amount (.01 inches)
#SNDP - Snow depth (.1 inches)
#FRSHTT – Indicator for occurrence of:
#		      Fog		
#                              Rain or Drizzle
#                              Snow or Ice Pellets
#                              Hail
#                              Thunder
#                              Tornado/Funnel Cloud

#
hist = df.hist(bins=10,figsize =(10,10))


# In[25]:


sns.histplot(data=df, x="WDSP", bins=10,kde=True,binwidth=2)


# In[27]:


sns.histplot(data=df, x="TEMP", bins=10,kde=True,binwidth=2) 


# In[28]:


#Mean temperature at this location since January 2021
df["TEMP"].mean()


# In[32]:


df[["TEMP","PRCP"]].median()


# In[33]:


df[["TEMP","PRCP"]].describe()


# In[34]:


df.agg(
    {
        "TEMP": ["min", "max", "median", "skew"],
        "PRCP": ["min", "max", "median", "mean"],
    }
)


# In[3]:



df1= pd.read_csv('NOAA_ALASKA_GlobalDaysummary2020.csv')
df1.tail(25)


# In[4]:


# PRCP_ATTRIBUTES -     
#           A = 1 report of 6-hour precipitation amount.
#                B = Summation of 2 reports of 6-hour precipitation amount.
#                C = Summation of 3 reports of 6-hour precipitation amount.
#                D = Summation of 4 reports of 6-hour precipitation amount.
#                E = 1 report of 12-hour precipitation amount.
#                F = Summation of 2 reports of 12-hour precipitation amount.
#                G = 1 report of 24-hour precipitation amount.
#                H = Station reported '0' as the amount for the day (eg, from 6-hour reports),
# but also reported at least one occurrence of precipitation in hourly observations. 
# This could indicate a trace occurred, but should be considered as incomplete 
# data for the day.
#                 I = Station did not report any precipitation data for the day and did not report any
#                      occurrences of precipitation in its hourly observations. It's still possible that
#                      precipitation occurred but was not reported.

#average precipitation by attribute
df1[["PRCP_ATTRIBUTES", "PRCP"]].groupby("PRCP_ATTRIBUTES").mean()


# In[5]:


df1.groupby("PRCP_ATTRIBUTES")["PRCP"].mean()


# In[6]:


#TEMP_ATTRIBUTES - Number of observations used in calculating mean temperature.
df1.groupby(["TEMP_ATTRIBUTES", "PRCP_ATTRIBUTES"])["PRCP"].mean()


# In[8]:


#number of observations in each precipitation attribute
df1["PRCP_ATTRIBUTES"].value_counts()


# In[ ]:





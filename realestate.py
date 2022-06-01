import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

import plotly
##plotly.offline.__init_notebook_mode()

import cufflinks as cf
##from IPython.display import display,HTML
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot  
cf.go_offline() 
##cf.set_config_file(theme='pearl',sharing='public',offline=True)


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

housing_data = pd.read_csv(r'C:\Users\anith\blog\realestate.csv')

print(housing_data.shape)

##housing_data = housing_data[['sqft_living', 'yr_built', 'condition','grade', 'price']]
housing_data = housing_data[['PRICE', 'SQFT', 'BED','BATH', 'FLOORS']]

print(housing_data.head())

print(housing_data.describe())

housing_data.iplot(kind='scatter', x='SQFT', y='PRICE', mode='markers', color = '#5d3087',  layout = {
        'title' :'Size vs Price',
        'xaxis': {'title': 'Size', 'type': 'log'},
        'yaxis': {'title': "Price"}
    })
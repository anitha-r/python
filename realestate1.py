#%%

from turtle import color, mode
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
cf.set_config_file(offline=False)


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


##housing_data.plot.scatter(x='SQFT',  y='PRICE', c='PRICE'
##        , s=10, colormap='viridis')


##housing_data.plot.scatter(x='BED',  y='PRICE', c='PRICE'
##        , s=10, colormap='viridis')

##housing_data.plot.scatter(x='BATH',  y='PRICE', c='PRICE'
##        , s=10, colormap='viridis')


X = housing_data[[ 'BED', 'SQFT']] 
y = housing_data['PRICE']

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) 

from sklearn.linear_model import LinearRegression  
reg = LinearRegression()  
reg.fit(X_train, y_train)

attributes_coefficients = pd.DataFrame(reg.coef_, X.columns, columns=['Coefficient'])  
print(attributes_coefficients)

y_pred = reg.predict(X_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(comparison)

from sklearn import metrics  
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))  
print('MSE:', metrics.mean_squared_error(y_test, y_pred))  
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  


# %%

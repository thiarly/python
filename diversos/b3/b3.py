from pandas.core.frame import DataFrame
import yfinance as yf
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = yf.download('PETR4.SA', start= '2021-02-01', end= datetime.datetime.today(), progress= False)
print (data)


data_sigmal = pd.DataFrame(index= data.index)
print (data_sigmal)

data_sigmal['price'] =data ['Close']
print (data_sigmal)

data_sigmal ['diferenca_diaria'] = data_sigmal ['price'].diff()
print (data_sigmal)

data_sigmal ['sinal'] = 0.0
print (data_sigmal)

data_sigmal ['sinal'] = np.where(data_sigmal['diferenca_diaria'] >0, 1.0, 0.0)
print (data_sigmal)

data_sigmal['positions'] = data_sigmal ['sinal'].diff()
print (data_sigmal)

capital_inicial = 1000.0

positions = pd.DataFrame(index= data_sigmal.index).fillna(0.0)

portfolio = pd.DataFrame(index= data_sigmal.index).fillna(0.0)

positions['PETR4'] = data_sigmal ['sinal']
portfolio['positions'] = (positions.multiply(data_sigmal['price'], axis= 0)).cumsum()

portfolio['cash'] = capital_inicial - (positions.diff().multiply(data_sigmal['price'], axis= 0)).cumsum()

portfolio['total'] = portfolio ['positions'] + portfolio ['cash']

print (portfolio)







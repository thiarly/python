import numpy as np
import pandas as ps
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf


yf.pdr_override()

## obtendos os dados do mercado

ibov = web.get_data_yahoo('^BVSP')

## Exibindo as cotação mais antigas

print (ibov.head())

## Exibindo as cotações mais recentes

print (ibov.tail())

## Plotando o gráfico com os preços de fechamento do Índice Bovespa

ibov["Low"].plot








####################################################
import yfinance as yf
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (18,8)
plt.style.use('seaborn-darkgrid')
#####################################################

# CRIANDO TABELAS COM OS DADOS DO ARQUIVO

# Fazendo o upload do arquivo base.xlsx
arquivo = pd.read_excel("/Users/thiarly/Documents/MEUSPROJETOS/python/diversos/b3/base.xlsx")

# Criando tabela com colunas para cada ativo e indexando por data
trade_quant = pd.pivot_table(arquivo, values='quantidade', index=['data'], columns=arquivo['ativo'].str.upper(), aggfunc=np.sum, fill_value=0)

# Criando tabela com colunas para cada ativo e indexando por data.
trade_price = pd.pivot_table(arquivo, values='preço', index=['data'], columns=arquivo['ativo'].str.upper(), fill_value=0)


# Baixando as cotações das ações
prices = yf.download(tickers=(trade_quant.columns+'.SA').to_list(), start=trade_quant.index[0], rounding=True)['Adj Close']
prices.columns = prices.columns.str.rstrip('.SA')


trades = trade_quant.reindex(index=prices.index)
trades.fillna(value=0, inplace=True)

aportes = (trades * trade_price).sum(axis=1)

posicao = trades.cumsum()

carteira = posicao * prices
carteira['saldo'] = carteira.sum(axis=1)


for i, data in enumerate(aportes.index):
    if i == 0:
        carteira.at[data, 'vl_cota'] = 1
        carteira.at[data, 'qtd_cotas'] = carteira.loc[data]['saldo'].copy()
    else:
        if aportes[data] != 0:
            carteira.at[data, 'qtd_cotas'] = carteira.iloc[i-1]['qtd_cotas']+(aportes[data] / carteira.iloc[i-1]['vl_cota'])
            carteira.at[data, 'vl_cota'] = carteira.iloc[i]['saldo'] / carteira.at[data, 'qtd_cotas']
            carteira.at[data, 'retorno'] = (carteira.iloc[i]['vl_cota'] / carteira.iloc[i-1]['vl_cota']) - 1
        else:
            carteira.at[data, 'qtd_cotas'] = carteira.iloc[i-1]['qtd_cotas']
            carteira.at[data, 'vl_cota'] = carteira.iloc[i]['saldo'] / carteira.at[data, 'qtd_cotas']
            carteira.at[data, 'retorno'] = (carteira.iloc[i]['vl_cota'] / carteira.iloc[i-1]['vl_cota']) - 1

plt.plot(carteira["vl_cota"])
plt.show()


"""
carteira['vl_cota'].plot()
#plt.plot(x["idade"])
#plt.hist(x["idade"])
#plt.hist(x["idade"],bins=20)
plt.pie(x["idade"], labels= x["nome"],autopct="%1.2f%%")
plt.show()
"""








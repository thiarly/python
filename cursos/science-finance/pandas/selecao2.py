"""
pandas.paydata.org

"""
# Importando pandas

#### Obtendo as cotações da VALE3 através de um arquivo CSV remoto
import pandas as pd
vale3 = pd.read_csv('https://raw.githubusercontent.com/codigoquant/data/main/VALE3.csv', index_col=0)
#print (vale3)


### Descobrindo o tipo de dado
#tipo = (type(vale3))
#print(tipo)

### Exibindo as 5 primeiras linhas
pri = (vale3.head())
#print (pri)

### Exibindo as ultimas 5 linhas
ult = (vale3.tail())
#print (ult)

### Selecionando a coluna com os precos maximos
colmax = vale3['High']
#print (colmax)

### Selecionando os precos maximos e de fechamento
colmaxfech = vale3[['High', 'Close']]
#print (colmaxfech)

### Selecionando linhas com .loc[]
### Selecionar os precos de outubro de 2020
out2020 = vale3.loc['2020-10-15']
#print (out2020)


### Selecionando os precos em 15/10/2020 e 19/10/2020
out1519 = vale3.loc[['2020-10-15', '2020-10-19']]
#print (out1519)

### Selecionando linhas e colunas com .loc[]
### Selecionando precos de abertura e fechamento dos dias 15/10/2020 e 19/10/2020
collinh = vale3.loc[['2020-10-15', '2020-10-19']] [['Open', 'Close']]
#print (collinh)

### Selecionando somente 2020 pra frente
ano2020 = vale3.loc['2020' :]
#print (ano2020)

### Fevereiro e Marco
fevmar = vale3.loc['2020-02':'2020-04']
#print(fevmar)

# Julho 2020
jul2020 = vale3.loc['2020-07' : '2020-08']
#print (jul2020)

# 13 e 23 de dezembro de 2019

dez1323 = vale3.loc['2019-12-13' : '2019-12-23']
#print (dez1323)

### Selecao por indice inteiro usando .iloc
# Selecionando a primeira linha
linhaone = vale3.iloc[0]
#print (linhaone)

# Selecionar a ultima linha
linhaout = vale3.iloc[-1]
#print(linhaout)

# Selecionar as tres primeiras linhas
linhatree = vale3.iloc[:3]
#print(linhatree)

# Selecionar as tres ultimas linhas
linhatreu = vale3.iloc[-3:]
#print(linhatreu)

# Selecionando as linhas 0, 6 e 8
linhazso = vale3.iloc[[0,6,8]]
#print (linhazso)

# Selecionando a primeira e segunda coluna
psc = vale3.iloc [:, :3] # :, -> referente a todas as linhas. :2 Referente a primeira e segunda coluna
print (psc)
#

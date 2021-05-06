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
print (vale3.head())

### Exibindo as ultimas 5 linhas
print (vale3.tail())

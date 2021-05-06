import numpy as np
import pandas as pd

df = pd.DataFrame({'col-0':[11,np.nan, np.nan,np.nan, 10],
                  'col-1':[12,np.nan, np.nan,np.nan, 20],
                  'col-2':[12, 23,np.nan,np.nan, 30],
                  'col-3':[14, 24, 34, np.nan, 40],
                  'col-4':[15, 25, 35, np.nan, 50]})



# Usando o dropna

clear = df.dropna()
#print(clear)

# Alterando o parametro how
haw = df.dropna(how='all')
#print(haw)

# Trabalhando com colunas
axis = df.dropna(axis=1)
#print (axis)

### Thresh
## Thresh = quantidade de valores nao-nan exigidos
# Exibir colunar com pelo menos 3 dados validos
thresh = df.dropna(axis=1, thresh=3)
#print (thresh)

# Exibir linhas com pelos menos 2 dados validos
th = df.dropna(thresh=4)
#print (th)

# Completando os valores com fillna
fillna = df.fillna(value='0')
#print(fillna)

# Prenchendo para tras com bfill
bfill = df.fillna(method='bfill')
#print(df)
#print('-*-'*30)
#print(bfill)


# Prenchendo para frente com ffill

ffill = df.fillna(method='ffill')
print('-*-'*30)
print()
print(df)
print('-*-'*30)
print()
print(ffill)




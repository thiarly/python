import pandas as pd

dados = {'produto':['TV','TV','sofa', 'sofa', 'geladeira', 'geladeira'],
        'vendedor': ['Maria', 'Paula', 'Paula', 'Vanessa', 'Jose', 'Jose'],
        'vendas':[20,13,34,11,8,12]}

df = (pd.DataFrame(dados))

# Agrupando por produto
dfe = (df.groupby('produto'))


# Somar valores
print('-'*15)
print('Somar valores')
sum = (df.groupby('produto')).sum()
print(sum)

# Desvio de valores
print('-'*15)
print('Desvio de valores')
std = (df.groupby('produto')).std()
print(std)

# Valores minimos
print('-'*15)
print('Valores minimos')
min = (df.groupby('produto')).min()
print(min)
# Valores máximos
print('-'*15)
print('Valores máximos')
max = (df.groupby('produto')).max()
print(max)
# Contagem de ocorrência
print('-'*15)
print('Contagem de ocorrência')
cont = (df.groupby('produto')).count()
print(cont)
# Resumo estátistico
print('-'*15)
print('Resumo estátistico')
des = (df.groupby('produto')).describe()
print(des)
# Transposição dos resultados
print('-'*15)
print('Transposição dos resultados')
tra = (df.groupby('produto')).describe().transpose()
print(tra)
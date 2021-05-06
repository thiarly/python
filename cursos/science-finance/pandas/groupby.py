import pandas as pd

dados = {'produto':['TV','TV','sofa', 'sofa', 'geladeira', 'geladeira'],
        'vendedor': ['Maria', 'Paula', 'Paula', 'Vanessa', 'Jose', 'Jose'],
        'vendas':[20,13,34,11,8,12]}

df = (pd.DataFrame(dados))
print(df)

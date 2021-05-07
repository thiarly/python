import pandas as pd

esquerda = pd.DataFrame({'chave': ['K0', 'K1', 'K2', 'K3'],
                            'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'chave': ['A=K0', 'K1', 'K2', 'K3','K4'],
                            'C': ['C0', 'C1', 'C2', 'C3', 'C4'],
                            'D': ['D0', 'D1', 'D2', 'D3', 'D4'],
                            'E': ['E0', 'E1', 'E2', 'E3', 'E4']})

merge = pd.merge(esquerda,direita)
print (merge)
print()
concat = pd.concat([esquerda,direita], axis=1)
print(concat)
print()
onhow = pd.merge(esquerda, direita, on='chave', how='inner') #inner, left, right e outer
print(onhow)
print()
print (esquerda)
print()
print(direita)                           


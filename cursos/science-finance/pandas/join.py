import pandas as pd

esquerda = pd.DataFrame({ 'A': ['A0', 'A1', 'A2'],
                          'B': ['B0', 'B1', 'B2']},
                      index = ['K0', 'K1', 'K2'])

direita = pd.DataFrame({ 'C': ['C0', 'C1', 'C2'],
                         'D': ['D0', 'D1', 'D2']},
                      index = ['K0', 'K2', 'K3'])
                            
print(esquerda)
print()
print(direita)
print()
print (esquerda.join(direita))
print()
print (esquerda.join(direita, how='outer'))

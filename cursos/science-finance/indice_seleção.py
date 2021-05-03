import numpy as np

vetor = np.arange(1, 25, 3)
print (vetor)
# Indexação e seleção por colchetes

"""
print (vetor[2])
print (vetor[1:3])
print(vetor[:6:2])
print(vetor[:])
print(vetor[:: -1])
"""
"""
# Atribuições de valores

print (vetor[:3])
#-----------------
vetor [:3] =100
print (vetor)
#-----------------
vetor_novo = vetor [:3]
print (vetor_novo)
#-----------------
vetor_novo[:] = 99
print(vetor_novo)
#-----------------
vetor_novo = vetor.copy()
print (vetor_novo)
#-----------------
"""
"""
# Selecionando elementos em Matrizes
print()
print('-' * 30)
matriz = np.array (([5,10,15], [20,25,30],[35,40,45]))
print (matriz)
print('-' * 30)
print (matriz[0])
print('-' * 30)
print(matriz[1][1])
print('-' * 30)
print(matriz[1,1])
print('-' * 30)
print(matriz[:,0])
print('-' * 30)
print(matriz[1:,1:])
"""

# Seleção condicional

print (vetor > 5)
print()

filtro = vetor > 5

print (vetor[filtro])

print(vetor[vetor < 5])

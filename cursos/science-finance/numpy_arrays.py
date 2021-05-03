"""
Numpy é uma biblioteca de ÁLGEBRA LINEAR para Python rápida pois tem seu core implementado em C.
É a base de muitas outras bibliotecas, como o Pandas que vamos ver a seguir.
"""
import numpy as np

lista = [1,2,3]

"""
# Criando Numpy Arrays
np_array = np.array(lista)

print (lista)
print (np_array)
print (type(np_array))

# Atributos e métrodo internos
## Arange
### Para um dado intervalo retorna valores igual espaçados a partir de um incremento fixo

print (np.arange(0,10))
print (np.arange(0,10, 0.1))

## Linspace
### Para um dado intervalo retorna igualmente espaçados a parti do número total de elementros fornecidos

print(np.linspace(0,10))
print(np.linspace(0,10,20))
print(np.linspace(0,10,20, endpoint=False))
"""
"""
# Zeros e Uns
print (np.zeros(4))
print()
print (np.zeros((3,3)))

print (np.ones(5))
print (np.ones((4,4)))
"""
"""
# Matriz identidade
## Cria uma matriz identidade
print (np.eye(5))
"""

# Gerador de números aleatórios (Random)
## rand
### Cria uma matrz de um dado formato e preenche com amostras aleatórias de uma distruição uniforme sobre [0, 1). rand9d0, d1, ..., dn)
"""
print (np.random.rand(2))
print()
print (np.random.rand(3,3,3))
"""
"""
### randn
print(np.random.randn(3,3))
print()
print(np.random.randint(1,10))
print(np.random.randint(1,10,3))
print()
print(np.random.randint(1,10,(5,5)))
"""
"""
vetor = np.random.randint(1,20,5)
print (vetor)
print(vetor.max())
print(vetor.argmax())
print(vetor.min())
"""
# Alternando o formato da Matriz
matriz = (np.arange(25))
print(matriz)
print(matriz.shape)
print(matriz.reshape(5,5))
matriz = (matriz.reshape(5,5))
print (matriz.shape)

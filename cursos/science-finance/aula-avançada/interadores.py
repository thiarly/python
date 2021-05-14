# Zip
esquerda = [2, 4, 6, 8, 10]
direita = [3, 6, 9, 12, 13]
for valor_esq, valor_dir in zip(esquerda, direita):
    print(valor_esq, valor_dir)


# map e filter
## map pega uma função e a aplica a cada valor de um iterador

# 0 a 9 ao quadrado
elevar_ao_quadrado = lambda x: x ** 2
for val in map(elevar_ao_quadrado, range(10)):
    print(val, end=' ')
print()

# filter é semelhante, exceto pelo fato de os valores passados serem avaliados como True:
## Valore pares até 10

eh_par = lambda x: x % 2 == 0
for val in filter(eh_par, range(10)):
    print(val, end=' ')
print()

filtro = lambda x: x > 2
for val in filter(filtro, range(10)):
    print(val, end=' ')
print()

# itertools
## itera sobre todas as permutações de uma sequência
from itertools import permutations
p = permutations('LUZ')
print(*p)

# itera sobre todas as combinações dentro de uma lista sem repetir
from itertools import combinations
c = combinations ('LUZ', 2)
print(*c)

from itertools import product
p = product('ab', range(3))
print(*p)
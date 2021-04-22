"""
Tuplas () -> Não Multavel
lista []  -> Multavel 
dicionario {}

APAGAR:
del lanche [3]
lanche.pop[3]
lanche.remove('pizza')

Caso n tenha pizza na lista, para n da um erro pode se fazer dessa forma.

if 'pizza' in lanche:
    lanche.remove('pizza')

CRIANDO UMA LISTA:
valores = list(range(4, 11))

ORDENAR:
valores = [8,2,5,6,7,8,1,3,4]
valores.sort() -> Ordem creceste
valores.sort(reverse=True) -> na ordem reversa
len(valores) -> vai contar quantos elementos tem na lista
"""

valores = []
valores.append(5)
valores.append(2)
valores.append(4)

for c, v in enumerate (valores):
    print (f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# AULA 17 (PAREI NO VIDEO 23')



"""
num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.insert(2, 2)
if 8 in num:
    num.remove(8)
else:
    print(f'Não achei o número {8}')
#num.sort()
print (num)
num.pop(0)
num.sort(reverse=True)
print (f'Essa lista tem {len(num)} elementos ')
"""
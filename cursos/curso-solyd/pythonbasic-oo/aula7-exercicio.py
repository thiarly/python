''''
(Metodo e Função)
EXERCICIO: Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção.
Faça outra função retorne o menor número dessa coleção.
'''

def maior(colecao):
    maior_item = colecao [0]
    for item in colecao:
       if item > maior_item:
           maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao [0]
    for item in colecao:
       if item < menor_item:
           menor_item = item
    return menor_item



print (menor ([-1,2,3,5,8,9,-100,200,3456]))


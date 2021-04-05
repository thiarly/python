"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor 
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvendo no desafio 108.
"""

import cash

p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {cash.moeda(p)} é R$ {cash.metade(p, True)}')
print (f'O dobro de R$ {cash.moeda(p)} é R$ {cash.dobro(p, True)}')
print (f'Aumento o {cash.moeda(p)} em 10% {cash.aumentar(p, 10, True)}')
print (f'O desconto de 10% em R$ {cash.moeda(p)} é R$ {cash.diminuir(p, 10, True)}')
print (f'O valor {cash.moeda(p)} multiplicado por 10x é {cash.multiplicar(p, True)}')

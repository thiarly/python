"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor 
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvendo no desafio 108.
"""

import moeda

p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')
print (f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print (f'Aumento o {moeda.moeda(p)} em 10% {moeda.aumentar(p, 10, True)}')
print (f'O desconto de 10% em R$ {moeda.moeda(p)} é R$ {moeda.diminuir(p, 10, True)}')
print (f'O valor {moeda.moeda(p)} multiplicado por 10x é {moeda.multiplicar(p, True)}')

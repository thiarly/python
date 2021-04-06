"""
Adapte o código do desafio 107, criando uma função adicional chamada() que consiga mostrar os valores como um valor
monetário formatdado.
"""

import moeda

p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.metade(p))}')
print (f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print (f'Aumento o {moeda.moeda(p)} em 10% {moeda.moeda(moeda.aumentar(p, 10))}')
print (f'O desconto de 10% em R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.diminuir(p, 10))}')
print (f'O valor {moeda.moeda(p)} multiplicado por 10x é {moeda.moeda(moeda.multiplicar(p))}')

"""
Adapte o código do desafio 107, criando uma função adicional chamada() que consiga mostrar os valores como um valor
monetário formatdado.
"""

import money

p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {money.moeda(p)} é R$ {money.moeda(money.metade(p))}')
print (f'O dobro de R$ {money.moeda(p)} é R$ {money.moeda(money.dobro(p))}')
print (f'Aumento o {money.moeda(p)} em 10% {money.moeda(money.aumentar(p, 10))}')
print (f'O desconto de 10% em R$ {money.moeda(p)} é R$ {money.moeda(money.diminuir(p, 10))}')
print (f'O valor {money.moeda(p)} multiplicado por 10x é {money.moeda(money.multiplicar(p))}')

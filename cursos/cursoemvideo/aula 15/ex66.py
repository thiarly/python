"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag.)
"""

cont = soma = 0

while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma = (soma + num)
    cont = (cont + 1)
if cont == 1:
    print (f'Você digitou {cont} vez e a soma total foi {soma}. ')
else:
    print (f'Você digitou {cont} vezes e a soma entre todos esses números foi {soma}.')


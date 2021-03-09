"""
Crie um programa que leia vários números inteiros pelo teclado.
No final mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

from typing import NoReturn


resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números com uma soma de {} e média {:.2} entre eles.'.format(quant, soma, media))
print ('O maior número foi {} e o menor número foi {}.'.format(maior, menor))




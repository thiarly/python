"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre:

A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$ 1.000,00
c - Qual é o nome do produto mais barato.
"""

maiorvalor = maisquemil = maisbarato = total = cont = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$ '))
    cont +=1
    total = total + valor
    if valor > 1000:
        maisquemil += 1
    
    if cont == 1:
        maisbarato = valor
        barato = produto
    else:
        if valor < maisbarato:
            menor = valor
            barato = produto 


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break


print ('{:-^20}'.format('FIM DO PROGRAMA'))
print (f'Total da compra R$ {total}')
print (f'Temos {maisquemil} custando mais que R$ 1000')
print (f'O produto de menor valor custa R$ {maisbarato}')
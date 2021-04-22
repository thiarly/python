"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A - Quantos números foram digitados.
B - A lista de valores, ordenada de forma decrescente.
C - Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Você quer continuar [S/N]: '))
    if resp in "Nn":
        break

print ('-'*30) 
print (f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print (f'A lista digitada digitada em forma decrescente {valores}')

if 5 in valores:
    print (f'O valor 5 foi ditado e adicionado a lista.')
else:
    print (f'O valor 5 não foi digitado.')

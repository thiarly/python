"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsideranco os espaços.

EX:
APOS A SOPA
A SACADA DA CASA
A TORRE DE DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

Faça um programa q leia a frase e diga se é um palidromo, vai desconsiderar os espaços
"""

frase = str(input('Digite uma frase: ')).strip().upper() #strip-> eliminou os espaços, upper-> jogou para maisculo
palavras = frase.split() #esplit-> esplitou as frases
junto = ''.join(palavras) #join-> juntou o split
inverso = junto[::-1]
print ('O inverso de {} é {}'.format(junto, inverso))

"""
#inverso = ''

for letra in range(len(junto) -1, -1, -1): #fez o inverso de junto
    inverso += junto [letra]
"""
print('\033[34m{}\033[m <-> \033[31m{}\033[m'.format(junto, inverso), end=' \n')

if inverso == junto:
    print('\033[36mÉ Palindromo\033[m')
else: 
    print('\033[36mNão é Palindromo\033[m')

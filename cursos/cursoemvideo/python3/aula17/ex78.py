"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final no final, mostre qual foi o maior e o menor valor digitado 
e sua respectivas posições na lista.
"""
listanum = []
maior = 0
menor = 0

for c in range(0, 5):
   listanum.append(int(input(f'Digite um valor para posição {c}: ')))
   if c == 0:
       maior = menor = listanum[c]
   else:
       if listanum[c] > maior:
           maior = listanum[c]
       if listanum[c] < menor:
           menor = listanum[c]
        
    
print ('-'*30)
print (f'Você digitou os valores {listanum}')

print (f'O maior valor digitado foi {maior} nas posiçãoes ',end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...',end='')
print ()


print (f'O menor valor digitado foi {menor} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end='')
print()



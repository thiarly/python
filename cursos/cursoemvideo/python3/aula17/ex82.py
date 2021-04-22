"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores:
pares e os valores impares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""




valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in "Nn":
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print (f'A lista completa: {valores}')
print (f'A lista de pares: {pares}')
print (f'A lista de impares: {impares}')




"""

if num % 2 == 0:
    pares.append(num)
else:
   
    impares.append(num)


print (f'Lista completa: {valores}')
print (f'Lista de números pares: {pares}')
print (f'Lista de números ímpares: {impares}')
"""

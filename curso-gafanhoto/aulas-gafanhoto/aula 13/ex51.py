"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))

decimo = primeiro + (10 - 1 ) * razão

print (decimo)

for cont in range(primeiro, decimo + razão, razão):
    print('{}'.format(cont), end= '-> ')

print ('\033[31mACABOU!\033[m')


"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário.
O Programa será interrompido quando o número solicitado for negativo.
"""


while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    print ('˜-'*20)
    if n < 0:
       break
    for c in range(1, 11):
        print (f'{n} x {c} = {n * c}')
    print ('˜-'*20)
    conf = ('Deseja fazer a tabuada de outro número? [S/N]').strip().upper()[0]
    

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
    



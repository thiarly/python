"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
import time 
def maior(* núm):
    cont = maior = 0
    print('-=-'*15)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        time.sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f'Foram informados {cont} valores ao todo. ')
    print (f'O maior valor informado foi {maior}. ')



#programa principal

maior(2, 9, 8, 5, 4, 2, 1)
maior(1, 8, 7)
maior(5, 8)
maior(6)
maior()
print()
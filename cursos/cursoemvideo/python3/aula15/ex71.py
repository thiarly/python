"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
"""

print('=' * 30)
print(f'{"BANCO DE CANUDOS":^30}')
print('=' * 30)
valor = float(input('Qual valor deseja sacar? '))
if valor < 1:
    print ('Valor inválidos! Os saques disponíves estão a parti de R$ 5 a R$ 100.')
    valor = float(input('Digite o valor novamente a sacar: '))
    
total = valor
ced = 100
totced = 0

while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print (f'Total de {totced} cédulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break
print ('='*30)
print ('Volte sempre ao BANCO DE CANUDOS, tenha um ótimo dia!')


   
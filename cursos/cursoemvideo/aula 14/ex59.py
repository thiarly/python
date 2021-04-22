"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = int(input('\033[033mDigite o 1º número:\033[m ')) 
n2 =int(input('\033[034mDigite o 2º número:\033[m '))
opcao = 0

while opcao != 5:

    print ("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVO NÚMEROS
[5] SAIR DO PROGRAMA""")
    opcao = int(input('>>>> Digite a sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print ('A soma entre: {} + {} é {}.'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicar = n1 * n2
        print ('A multiplicação entre: {} e {} é {}'.format(n1, n2, multiplicar))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
            print ('Entre {} e {} o maior número é {} '.format(n1, n2, maior))
        else:
            print ('Entre {} e {} não existe maior número os dois são iguais.'.format(n1, n2))

    elif opcao == 4:
        print ('Informe os números novamente: ')
        n1 = int(input('\033[033mDigite o 1º número:\033[m ')) 
        n2 =int(input('\033[034mDigite o 2º número:\033[m '))
    
    elif opcao == 5:
        print ('Finalizando...')
    
    else:
        print ('Opção inválida, Tente novamente!')

    print ('\033[035m=-=\033[m'*20)
    sleep(2)

print ('Fim do programa, volte sempre!')




    




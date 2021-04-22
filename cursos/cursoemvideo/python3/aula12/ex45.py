#Crie um programa que faça o computador jogar JOKENPÔ com você.
from random import randint
from time import sleep

itens =('Pedra', 'Papel', 'Tesoura')

computador = randint (0, 2)

print (''' Suas Opções :
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

 
jogador = int(input('Qual é a sua jogada? '))

print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
#mostrando o que cada um jogou
#print('-=' * 15)
#print (f'Computador jogou: {itens[computador]}')
#print (f'Jogador jogou: {itens[jogador]}')
#print ('-=' * 15)


print('-=' * 15)
print ('Computador jogou: {}'.format(computador))
print ('Jogador jogou: {}'.format(jogador))
print ('-=' * 15)

#montando a estrura condicional para apresentar o resultado

#---------------------------------------------------------
if computador == 0: # Computador jogou PEDRA
    if jogador == 0: 
        print ('EMPATE!')

    elif jogador ==1:
        print ('JOGADOR VENCEU!')

    elif jogador ==2:
        print ('COMPUTADOR VENCEU!')
    
    else:
        print ('JOGADA INVÁLIDA!')
#--------------------------------------------------------
if computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print ('COMPUTADOR VENCEU!')
    
    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCEU!')
    
    else:
        print('JOGADA INVÁLIDA!')
#--------------------------------------------------------
if computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print ('JOGADOR VENCEU!')

    elif jogador == 1:
        print ('COMPUTADOR VENCEU!')
    
    elif jogador == 2:
        print ('EMPATE!')

    else:
        print('JOGADA INVÁLIDA!')



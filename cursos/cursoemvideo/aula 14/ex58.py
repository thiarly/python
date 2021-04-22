"""
Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.

"""


#########################################################################################
from random import randint
computador = randint (0,10)
print('\033[032m=-\033[m'*33)
print('\033[031m->\033[m Sou seu computador... acabei de pensar em um número de 0 a 10.')
print('\033[031m->\033[m Será que você consegue adivinhar qual foi?')
print('\033[032m=-\033[m'*33)
##########################################################################################
acertou = False
palpites = 0
##########################################################################################
while not acertou:
    jogador = int(input('\033[034mQual o seu palpite?\033[m '))
    palpites =+ 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[032mMais... Tente mais uma vez.\033[m ')
        elif jogador > computador:
            print('\033[031mMenos... Tente mais uma vez.\033[m')


print ('\033[035mAcertou com {} tentativas. Parabéns!\033[m'.format(palpites))










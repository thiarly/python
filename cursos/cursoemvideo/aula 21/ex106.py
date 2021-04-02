"""
Faça um mini-sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""
from time import sleep
c = ('\033[m', # 0 - sem cor
     '\033[0;30;41m' # 1 vermelho
     '\033[0;30;42m' # 2 verde
     '\033[0;30;43m' # 3 amarelo  
     '\033[0;30;44m' # 4 azul  
     '\033[0;30;45m' # 5 roro
     '\033[7;30m'    # 6 branco      
    );

def ajuda (com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print (c[6], end='')
    help(com)
    print (c[0], end='')

def título(msg, cor =0):
    tam = len(msg) + 4
    print (c[cor], end=' ')
    print('~' * tam)
    print (f'{msg}')
    print ('~' * tam)
    print ([0], end=' ')
    sleep(1)

#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input(input("Função ou Biblioteca > ")))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
 
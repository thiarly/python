#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


#IDADE PARA SE ALISTAR AOS 18 ANOS.

nome = str(input('Digite seu nome: '))
ano = float(input('Digite o ano de nascimento: '))

c = 2021 - ano

if c < 18:
    print('{}, você ainda não está com a idade para alistamento no serviço militar.'.format(nome))
elif c == 18:
    print('{}, você está no periodo de alistamento no serviço militar.'.format(nome))
else:
    print('{}, você já passou do tempo de alistamento no serviço militar.'.format(nome))

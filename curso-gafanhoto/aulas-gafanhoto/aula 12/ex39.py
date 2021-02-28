#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


#IDADE PARA SE ALISTAR AOS 18 ANOS.

from datetime import date
atual = date.today().year

nome = str(input('Digite seu nome: '))
ano = float(input('Digite o ano de nascimento: '))

idade = atual - ano
print('Quem nasceu em {:.0f} tem {} anos em {}'.format(ano, idade, atual))


#c = 2021 - ano

if idade == 18:
    print('{}, você precisa se alistar imediatamente.'.format(nome))
elif idade < 18:
    saldo = 18 - idade
    print('{}, ainda falta {:.0f} anos para o alistamento.'.format(nome, saldo))
    a = atual + saldo
    print ('Seu alistamento será em {:.0f} anos.'.format(a))
else:
    saldo = idade - 18
    print('{}, você já deveria ter se alistado a {:.0f} anos.'.format(nome, saldo))
    a = atual - saldo
    print ('Seu alistamento foi em {:.0f} anos.'.format(a))
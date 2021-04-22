"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de uma jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar o ficha jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(jog='Desconhecido', gol=0):
    print (f'O jogador {jog} fez {gol} gol(s) no campeonato')


#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.
"""

jogador = {}
partidas = list()
jogador ['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
jogador ['gols'] = partidas[:]
jogador ['total'] = sum(partidas)
print ()
print ('-=-'*20)
print ()
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print ()
print ('-=-'*20)
print ()
print (f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in  enumerate (jogador['gols']):
    print (f' ==> Na partida {i+1}, fez {v} gols.')
print (f' ==> Foi um total de {jogador["total"]} gols.')



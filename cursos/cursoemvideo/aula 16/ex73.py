"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do compeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da Flamengo.
"""

times = ('Flamengo', 'Internacional','Atlético','São Paulo',
'Fluminense','Grêmio','Palmeiras','Santos','Athletico','Bragantino',
'Ceará','Corinthians','Atlético','Bahia','Sport','Fortaleza','Vasco',
'Goiás','Coritiba','Botafogo')

co = int(input('''
[ 1 ] Imprimir os 5 primeiros colocados:
[ 2 ] Imprimir os 4 últimos colocados:
[ 3 ] Mostre a classificação em ordem alfabética
[ 4 ] Em que posição da tabela está o Flamengo
sua opção: '''))


if co == 1:
    print ((f'Os 5 primeiros colocados do compeonato brasileiro 2020: ->>: {times [0:5]}'))
elif co == 2:
    print ((f'Os 4 últimos colocados do campeonato brasileiro 2020: ->>: {times [16:]}'))
elif co == 3:
    print (f'Times em ordem alfabética: {sorted(times)}')
elif co == 4:
    print (f'O flamengo está na {times.index("Bahia")+1} posição.')
else: 
    print ('Opção inválida!')




"""
print ((f'Os 5 primeiros colocados do compeonato brasileiro 2020: ->>: {times [0:5]}'))
print ((f'Os 4 últimos colocados do campeonato brasileiro 2020: ->>: {times [16:]}'))
print (f'Times em ordem alfabética: {sorted(times)}')
print (f'O flamengo está na {times.index("Bahia")+1} posição.')
"""

"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""


print ('-='*8)
print ('GERADOR DE PA')
print ('-='*8)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1


while cont < 10:
    print ('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')



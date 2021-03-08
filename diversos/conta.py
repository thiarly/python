"""
wey = 199
treinador = 200
fisio = 85
energy1 = 47.12
energy2 = 47.12
"""

from time import sleep

print ('-˜='*20)
print ('\033[032mCONTA ESPORTE MENSAL\033[m')
print ('-˜='*20)

sleep(2)
cont = 0

s = 0
while True:
    suplementação = float(input('Digite o valor dos suplementos R$: '))
    confirma = str(input('Deseja adicionar mais algum suplemento? [S/N]: ')).strip().upper()[0]
    if confirma in 'Nn':
        break
    s = (s + suplementação)
print (s)

##################################################################################
treinador = float(input('Digite o valor do treinador R$: '))
fisioterapia = float(input('Digite o valor da fisioterapia R$: '))
material = float(input('Digite o valor dos materiais R$: '))
##################################################################################
tre = treinador
sup = suplementação
fis = fisioterapia
mat = material
soma = treinador + suplementação + fisioterapia
##################################################################################
p1 = (sup / soma) * 100
p2 = (fis / soma) * 100
p3 = (tre / soma) * 100
p4 = (mat / soma) * 100
##################################################################################
print ('\033[034mSuplemento R$ {:.2f} / ({:.2f}%)\033[m'.format(sup, p1))
print ('\033[033mFisioterapia R$ {:.2f} / ({:.2f}%)\033[m'.format(fis, p2))
print ('\033[032mTreinador R$ {:.2f} / ({:.2f}%)\033[m'.format(tre, p3))
print ('\033[031mValor total R$ {:.2f}\033[m'.format(soma))
##################################################################################





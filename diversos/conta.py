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

suplementação = 0
while True:
    s = float(input('Digite o valor dos suplementos R$: '))
    c = str(input('Deseja adicionar mais algum suplemento? [S/N]: ')).strip().upper()[0]
    suplementação = (suplementação + s) 
    cont = cont + 1
    if c in 'Nn':
        break

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
print ('Foram \033[034m{}\033[m produtos de suplementos com total \033[034mR$ {:.2f}\033[m e porcetagem \033[034m{:.2f}%\033[m'.format(cont, sup, p1))
print ('Fisioterapia \033[033mR$ {:.2f}\033[m / \033[033m{:.2f}%\033[m'.format(fis, p2))
print ('Treinador \033[032mR$ {:.2f}\033[m / \033[032m{:.2f}%\033[m'.format(tre, p3))
print ('Valor total \033[031mR$ {:.2f}\033[m'.format(soma))
##################################################################################





#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

v = float(input('Qual a velocidade do carro? '))

if v > 80:
    print ('Você foi multado por tráfegar a {}KM/H, velocidade permitidade de 80KM/H'.format(v))

c = (v - 80) * 7

print ('Valor da multa a pagar R$ {}.'.format(c))







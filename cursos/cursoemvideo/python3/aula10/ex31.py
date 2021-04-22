#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM E R$ 0,45 para viagem mais longas.

km = float(input('Qual a distância em KM da viagem? '))

if km <= 200:
    v = 0.50 * km
    print ('O preço da passagem é {}.'.format(v))
else:
    v = 0.45 * km
    print ('O preço da passagem é {}.'.format(v))
    

#Crie um programa que leia um número INTEIRO e mostre na tela se ele é PAR ou íMPAR.

numero = int(input('Digite um número inteiro: '))

if (numero%2) == 0:
    print ('O número digitado {}, é PAR.'.format(numero))
else:
    print ('O numéro digitado {}, é íMPAR.'.format(numero))


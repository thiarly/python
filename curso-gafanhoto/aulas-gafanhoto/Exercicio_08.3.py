#Crie um programa q leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

#Ex: Digite um número 6.127, o número 6.127 tem a parte inteira 6

import math 
number = float(input('Digite uma número do tipo Float: '))
inteiro = math.floor(number)
print ('Resultado inteiro é: {}'.format(inteiro))












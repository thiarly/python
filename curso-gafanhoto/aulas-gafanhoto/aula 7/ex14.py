# Escreva um programa que converta uma temperatura digitada em ºC (Grau Celsius) e a converta para ºF (Grau Fahrenheit).


temperatura = float(input('Digite a temperatura em ºC: '))

conversor = temperatura * 9 / 5 + 32


print ('A temperatura de {}ºC, é igual a {}ºF'.format(temperatura, conversor))

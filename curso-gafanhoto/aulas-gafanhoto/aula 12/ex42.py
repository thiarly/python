#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo do triângulo será formado:
# Equilátero: todos os lados iguais
# Isóscelas: dois lados iguais
# Escaleno: todos os lados diferentes.

print ('-='*20)
print ('Analisador de Triângulo')
print ('-='*20)
r1 = float(input('Digite a 1º primeira metragem: '))
r2 = float(input('Digite a 2º primeira metragem: '))
r3 = float(input('Digite a 3º primeira metragem: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Com essas medidas é possível formar um triângulo: ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÔSCELES')
else:
    print ('Com essas medidas não é possível formar um triângulo.')
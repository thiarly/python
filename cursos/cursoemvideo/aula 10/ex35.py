#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print ('-='*20)
print ('Analisador de Triângulo')
print ('-='*20)
r1 = float(input('Digite a 1º primeira metragem: '))
r2 = float(input('Digite a 2º primeira metragem: '))
r3 = float(input('Digite a 3º primeira metragem: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Com essas medidas é possível formar um triângulo.')
else:
    print ('Com essas medidas não é possível formar um triângulo.')


#print (lista)


#print (lista.append())




#print ('O menor número digitado foi {:.0f}'.format((lista)))
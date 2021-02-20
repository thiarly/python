#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('Digite o 1º número: '))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3º número: '))

#Descobrindo o menor número
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Descobrindo o maio número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print ('O menor valor digitado foi {}'.format(menor))
print ('O maior valor digitado foi {}'.format(maior))





#lista = [n1, n2, n3]

#print ('O maior número digitado foi {:.0f}.'.format(max(lista)))
#print ('O menor número digitado foi {:.0f}'.format(min(lista)))





#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem:

# O primeiro valor é maior
# O Segundo valor é maior
# Não existe valor maior, os dois são iguais


n1 =  float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print ('O primeiro valor é maior. ')
elif n1 < n2:
    print ('O segundo valor é maior. ')
#elif n1 == n2:
     #print ('Não existe valor maior, os dois são iguais. ')
else:
    print ('Não existe valor maior, os dois são iguais. ')
#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúscular e minusculas
# Quantas letras ao todo (sem considerar o espaço)
# Quantas letras tem o primeiro nome.

name = str(input('Qual o nome? ')).strip() #.strip -> para eliminar os espaços antes e dopois do nome.

print ('Seu nome maiusculo é: {}'.format(name.upper()))
print ('Seu nome minusculo é: {}'.format(name.lower()))
print ('Seu nome sem considerar espaço tem essa quantidade de letras {}'.format(len(name) - name.count(' '))) # - name.count, diminuindo os espaços.
separa = name.split()
############################################################################
print ('Seu 1º nome tem essa quantidade de letra {}'.format(len(separa[0])))
############################################################################
print ('Seu 1º nome tem essa quantidade de letra {}'.format(name.find(' ')))
############################################################################









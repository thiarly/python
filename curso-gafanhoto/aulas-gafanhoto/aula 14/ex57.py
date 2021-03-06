"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # [0] -> Para pegar apenas a primeira letras, dessa forma M ou F.
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Por favor, informe seu sexo novamente, com [M/F]: ')).strip().upper()[0]
print('Sexo registrado com sucesso!'.format(sexo))



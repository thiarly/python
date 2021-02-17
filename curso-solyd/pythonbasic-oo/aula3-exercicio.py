'''
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decida se ela está apta a ser do exercito
para entrar no exercicio é preciso ter mais de 18 anos pesar mais ou igual 60 kilos e medir mais ou igual 1.70 metros
'''

idade = int(input ('Escreva sua idade:'))
peso = float(input ('Informe seu peso:'))
altura = float(input ('Informe a sua altura:'))


print(type(idade),type(peso),type(altura))


if idade >= 18 and peso >= 60 and altura >= 1.70:
    print ('Voce esta apto a servir o exercicito')
else:
    print ('Voce nao esta apto')











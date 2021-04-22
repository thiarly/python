"""
Crie um programa que leia a idade e o sexo de várias pessoas cadastradas. O programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:

A - QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
B - QUANTOS HOMENS FORAM CADASTRADOS.
C - QUANTAS MULHERES TEM MENOS DE 20 ANOS.

"""

tot18 = toth = tot20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == "M":
        toth = toth + 1   
    if sexo == "F" and idade < 20:
        tot20 = tot20 +1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas maiores que 18 anos foram {tot18}')
print (f'Foram cadastrados no total {toth} homens.')
print (f'Foram cadastradas {tot20} mulheres menores que 20 anos')
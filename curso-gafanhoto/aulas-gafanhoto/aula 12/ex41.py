# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#... e mostre sua categoria, de acordo com a idade:

# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# acima: MASTER

nome = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))

c = 2021 - ano

if c <= 9:
    print('{}, você está na categoria: MIRIM.'.format(nome))
elif c <= 14:
    print ('{}, você está na categoria: INFANTIL.'.format(nome))
elif c <= 19:
    print ('{}, você está na categoria: JUNIOR.'.format(nome))
elif c <= 20:
    print ('{}, você está na categoria: SÊNIOR.'.format(nome))
else:
    print ('{}, você está na categoria: MASTER.'.format(nome))



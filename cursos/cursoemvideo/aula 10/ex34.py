#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o seu salário: '))

if s >= 1250:
    s1 = (s + (s * 10) / 100  )
    print ('O seu novo salário com reajuste de 10% ficou R$ {}'.format(s1))
else:
    s1 = (s + (s * 15 ) / 100 )
    print('O seu novo salário com reajuste de 15% ficou R$ {}'.format(s1))

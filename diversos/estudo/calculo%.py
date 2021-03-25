sal = float(input('Salário: R$ '))
com = float(input('Comissão: R$ '))
aju = float(input('Reembolso: R$ '))

com = (com / sal) * 100
aju = (aju / sal) * 100

print (f'{com:.2f}%')
print (f'{aju:.2f}%')
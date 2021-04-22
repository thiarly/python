#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu salário: R$ '))

reajuste = 15
aumento = salario + (salario * 15) / 100 

print('Com o aumento de {}% o seu novo salário é R$ {:.2f}'.format(reajuste, aumento))


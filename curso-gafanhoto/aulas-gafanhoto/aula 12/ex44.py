#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinhieiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print ('Qual a forma de pagamento que deseja? ')
print ('1. Dinheiro ')
print ('2. Cheque ')
print ('3. À vista no cartão. ')
print ('4. Em até 2x cartão ')
print ('5. 3x ou mais no cartão')


c = int(input('Informe a condição de pagamento: '))

#dinheiro = 1
#cheque = 2
#vista = 3
#cartaov = 4
#cartaop = 5

print (c)


if c == 1:
    print('Você tem um desconto de 10%')

elif c == 2:
    print('Você tem um desconto de 10%')

elif c == 3:
    print('Você tem 5% de desconto')

elif c == 4:
    print('Você pode parcelar em até 2x no cartão sem juros')

elif c == 5:
    print ('Parcelar acima de 3x no cartão acrescenta 20% de juros ')

else:
    print ('Forma de pagamento não existe! ')




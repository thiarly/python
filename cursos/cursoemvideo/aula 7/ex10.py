#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Si

# Considere que US$ 1,00 = 5.20

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.20

print ('Você tem esse valor na carteira R$ {:.2f}'.format(real))
print ('Em dolar tem esse valor US$ {:.2f}'.format(dolar))




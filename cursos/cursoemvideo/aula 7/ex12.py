#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o preço do produto:R$ '))

desconto = (valor - (valor * 5) / 100)
aumento = (valor + (valor * 5 / 100))

print('O produto que você está levando tem 5% de desconto, novo valor com desconto R$ {:.2f}'.format(desconto))
print('O produto que você está levando teve um aumento de 5%, novo valor do produto R$ {:.2f}'.format(aumento))


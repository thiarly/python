#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa
#... o salário do comprador e em quando anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
ano = int(input('Em quantos anos pretende pagar a casa? '))



s = ano * 12

prestação = casa / (ano * 12)
minimo = salario * 30 / 100

print ('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, ano), end='')
print (' A prestação será de R$ {:.2f}'.format(prestação))

if prestação <= minimo:
    print ('Emprestimo aprovado! Valores das parcelas {}.'.format(minimo))
else:
    print ('Emprestimo recusado! ')



#% = (salario * 30) / 100


#print ('Valor da prestão {:.2f}'.format(prestação))
#print ('Valor máximo da prestão {:.2f}'.format(minimo))



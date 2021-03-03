#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinhieiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS CANUDOS BAHIA '))


preço = float(input('Preço das compras: R$ '))

print (''' FORMAS DE PAGAMENTO
[ 1 ]. Dinheiro ')
[ 2 ]. Cheque ')
[ 3 ]. À vista no cartão
[ 4 ]. Em até 2x cartão
[ 5 ]. 3x ou mais no cartão''')

c = int(input('Qual é a opção? '))



if c == 1:
    total = preço - (preço * 10 / 100)
    print ('Compra no dinheiro tem desconto de 10%. Valor total R$ {:.2f} e valor com desconto {:.2f}'.format(preço, total))

elif c == 2:
    total = preço - (preço * 10 / 100)
    print ('Compra no cheque tem desconto de 10%. Valor total R$ {:.2f} e valor com desconto {:.2f}'.format(preço, total))

elif c == 3:
    total = preço - (preço * 5 / 100)
    print ('Compra no cartão a vista tem desconto de 5%. Valor total R$ {:.2f} e valor com desconto {:.2f}'.format(preço, total))

elif c == 4:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))

elif c == 5:
    total = preço + (preço * 20 / 100)
    totaparc = int(input('Quantas parcelas? '))
    parcela = total / totaparc
    print ('Sua comrpa será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totaparc, parcela))
    print ('Valor total da compra {:.2f}'.format(total))
else:
    total = preço
    print ('Forma de pagamento não existe! ')




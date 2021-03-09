#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
#... de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
#... e R4 0,15 por KM rodado

name = str(input('Digite o nome do locatário: ')) 
modelo = str(input('Digite o modelo do carro locado: '))
quantidade = int(input('Digite a quantidade de diária locada: '))
quilometro = float(input('Digite a quantidade de KM percorrido: '))

# Calculo direto 
# pago = (quantidade * 60) + (quilometro * 0.15)

diaria = quantidade * 60
km = quilometro * 0.15
soma = diaria + km

print ('Valor referente as diarias: R$ {:.2f}'.format(diaria))
print ('Valor refente aos KMs percorridos R$ {:.2f}'.format(km))
print ('O valor total da locação ficou R$ {:.2f}'.format(soma))




#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#Para - Binário
#Para - Octal
#Para - Hexadecimal

# Como converter números em Python?



num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')


opcão = int(input('Sua Opção: '))

if opcão == 1:
    print ('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcão == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcão == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print ('Opção inválida. Tente novamente!')

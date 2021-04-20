

operacao = str(input('Qual operação deseja executar? (+,*,-,/) '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o seguro número: '))

if operacao == '+':
    total = num1 + num2
    print (total)
elif operacao == '*':
    total = num1 * num2
    print (total)
elif operacao == '-':
    total = num1 - num2
    print(total)
elif operacao == '/':
    total = num1 / num2
    print (total)
else:
    print('Opção inválida, execute o programa novamente!')
from time import sleep

print('-'*40)
print ('\033[1;33mBEM VINDO A CALCULADORA BÁSICA\033[m')
print('-'*40)

sleep(2)
print()

num1 = float(input('\033[1;32mDigite o primeiro número:\033[m '))

while True:
    operacao = str(input('Qual operação deseja executar? (+, * , - ou /): -> '))
    if operacao not in '+*-/':
        print('\033[1;31mOpção inválida, tente novamente, as opções disponíveis são: (+,*,-,/)\033[m')
        break

    num2 = float(input('\033[1;32mDigite o segundo número:\033[m '))

    if operacao == '+':
        total = num1 + num2
        print(f'\033[1;34m{num1} + {num2} é = {total}\033[m')
        break

    elif operacao == '*':
        total = num1 * num2
        print(f'\033[1;34m{num1} * {num2} é = {total}\033[m')
        break

    elif operacao == '-':
        total = num1 - num2
        print(f'\033[1;34m{num1} - {num2} é = {total}\033[m')
        break

    elif operacao == '/':
        total = num1 / num2
        print(f'\033[1;34m{num1} / {num2} é = {total}\033[m')
        break




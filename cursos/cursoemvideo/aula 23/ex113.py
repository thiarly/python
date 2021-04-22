"""
Reescreva a função leialnt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também função leiaFloat()
com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número float válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor Float: ')
print(f'O valor inteiro digitado foi {n1} e o float foi {n2}')

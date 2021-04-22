def ajuda(funcao):
    print('\033[7m~' * 30)
    help(funcao)
    print('\033[m' * 30)


while True:
    print('\033[45m~'*30)
    print(f'{"Sistema de ajuda PyHELP":^30}')
    print('~' * 30)
    print('\033[m')

    aux = (str(input('Função ou Biblioteca (FIM para sair)-> ')))
    if aux == 'FIM':

        break

    ajuda(aux)
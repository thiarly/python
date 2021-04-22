"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individual.
"""

"""
('BUG PARA FINALIZAR, RESOLVER!')
"""


ficha = list ()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    if nota1 > 10:
        print ('Nota inválida, execute o programa novamente.')
        print ('Nota válida é entre 1 e 10.')
        break
    else: 
        print ('Nota adicionada com sucesso!')
    nota2 = float(input('Nota 2: '))
    if nota2 > 10:
        print ('Nota inválida, execute o programa novamente.')
        print ('Nota válida é entre 1 e 10.')
        break
    else: 
        print ('Nota adicionada com sucesso!')

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media ]) # [nome, =0  [nota1, nota2] = 1, media = 2 ]
    resp = str(input('Quer continuar [S/N]: '))
    
    if resp in "Nn":
        print ('-='*30)
        print (f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
        print ('-='*30)
        for i, a in enumerate(ficha):
            print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

        while True:
            print ('-='*30)
            opc = int(input('Mostrar nostas de qual aluno? (999 interrompe): '))
            if opc == 999:
                print ('FINALIZANDO...')
                break
            if opc <= len(ficha) -1:
                print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print ('\033[033m<<< VOLTE SEMPRE >>>\033[m')
        

        
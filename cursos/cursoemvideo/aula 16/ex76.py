"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizado os dados em forma tabular.
"""

listagem = ('Caneta', 1.70,
            'Borracha', 1,
            'Caderno', 20,
            'Marca texo', 5.50,
            'Pincel', 28,
            'Case Notebook', 250,
            'Lousa', 120,
            'Estojo', 5,
            'Livro', 45)

print ('-'*45)
print (f'{"LISTAGEM DE PREÇO":^45}')
print ('-'*45)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print (f'{listagem[pos]:.<35}',end='')
    else:
        print (f'R$ {listagem[pos]:.2f}')

print ('-'*45)


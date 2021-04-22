#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = str(input('Escreva o nome do 1º aluno: '))
a2 = str(input('Escreva o nome do 2º aluno: '))
a3 = str(input('Escreva o nome do 3º aluno: '))
a4 = str(input('Escreva o nome do 4º aluno: '))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O aluno sorteado foi: {}.'.format(sorteio))

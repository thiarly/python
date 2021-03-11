"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'esporte', 'natacao', 'bike', 'run',
            'em', 'busca', 'liberdade', 'financeira')

for c in palavras:
    print (f'\nNa palavra {c.upper()} temos:->  ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')



"""
- Interactive Help
- Docstrings
- Parametros opcionais
- Escopo de váriaveis
- Retorno de resultados
"""

#RETORNO DE RESULTADOS

def somar (a, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(1, 2, 3)
r2 = somar(3, 4)
r3 = somar(8)

print (f'Os resultados foram {r1}, {r2}, {r3}')

#def teste(a, b=1, c=2)
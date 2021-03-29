"""
- Interactive Help
- Docstrings
- Parametros opcionais
- Escopo de váriaveis
- Retorno de resultados
"""

#RETORNO DE RESULTADOS

def somar (a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(4, 6, 10)
r2 = somar(4, 9)
r3 = somar(8)

print (f'Os resultados foram {r1}, {r2}, {r3}')


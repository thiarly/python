"""
- Interactive Help
- Docstrings
- Argumentos opcionais
- Escopo de váriaveis
- Retorno de resultados
"""

# INTERRACTIVE HELP
def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :pagam f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """

    c = i
    while c <= f:
        print (f'{c}', end='..')
        c += p
    print ('FIM!')

contador (0, 100, 2)

help (contador)

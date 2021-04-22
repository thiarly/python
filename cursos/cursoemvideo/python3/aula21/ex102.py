"""
Crie uma programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
que será uma valor lógico (opcional) inidicando se será mostrado ou não na tela o processo de cálculo do tatorial.
"""
#####################################################
def fatorial (n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print (c, end=' ')
            if c > 1:
                print (' x ', end=' ')
            else:
                print (' = ', end=' ')
        f *= c
    return f
######################################################

#Programa principal
print(fatorial(5, show=True))
#import numpy_financial as npf

# Valor presente
# Se uma pessoa deseja obter R$ 20.000,00 dentro de um ano, quanto deverá ela depositar na poupança que rende 0,2% de juros composto ao mês?

"""
PV = FV / (1 + R)n
"""

"""
fv = 20000 # Valor investido
i = 0.002 # Taxa
n = 12 # Meses

(npf.pv(i, n, 0, fv))
"""
#print(npf.pv(0.05, 5, 0, 10_000))

#pv = npf.pv(i, n, 0, fv=0)












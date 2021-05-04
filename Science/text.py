import numpy_financial as npf


#######################################################################
# Valor presente
# Se uma pessoa deseja obter R$ 20.000,00 dentro de um ano, quanto deverá ela depositar na poupança que rende 0,2% de juros composto ao mês?

"""
PV = FV / (1 + R)n
"""

"""
fv = -20000 Valor a receber
i = 0.002 # Taxa 0.2% a.m
n = 12 # Meses 
pv = (npf.pv(i, n, 0, fv))
print(f'Deposito Inicial Necessario = R$ {pv:.2f}')
"""
######################################################################
# Valor futuro (FV)
## FV = PV(1+r)n
"""
pv = 10000 # Valor investido
n = 8 # Meses 
i = 0.005 # Taxa 0.5% a.m
fv = (npf.fv(i, n, 0, pv))
print(f'Valor de restage = R$ {fv:.2f}')
"""
#######################################################################
# Valor presente Liquido (NPV)
"""
Uma empresa esteja avaliando um investimento no valor de R$ 750.000,00 do qual esperam-se beneficios anuais de caixa de R$ 250.000,00
no primeiro ano, R$ 320.000,00 no segundo ano, R$ 380.000,00 no terceiro ano de R$ 280.000,00 no quarto ano.

A empresa definiu em 20% ao ano a taxa de desconto a ser aplicada aos fluxos de caixa de investimento.
"""
"""
vpl = (npf.npv(0.2, [-750000, 250000, 320000, 380000, 280000]))
print(f'VPL = R$ {vpl:.2f}')

"""
#######################################################################
# Taxa interna de retorno (IRR)
"""
A taxa interna de retorno e uma taxa de desconto hipotetico que, quando aplicada a um fluxo de caixa, faz com que os valores das despesas
trazidos ao valor presente, seja aos valores dos retornos invesitmentos, tambem trazidos ao valor presente
Ex:
Admita que um investimento de R$ 70.000,00 gere caixa de R$ 20.000,00, R$ 40.000,00, R$ 45.000,00 e R$ 30.000,00, respectivamente,
ao final dos proximos quatro anos.
"""

tir = (npf.irr([-70000,20000,40000,45000,30000]))
print (f'TIR = R$ {tir:.2%}')
#######################################################################





 









# print(npf.pv(0.05, 5, 0, 10_000))


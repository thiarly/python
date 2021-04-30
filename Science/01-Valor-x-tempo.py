"""
Qual seria o valor futuro (FV) se eu investisse R$ 1000 por 1 ano, com um retorno de 5% ao ano
FV = PV (1 + R) N


PV = FV / (1+r) ** n
"""


pv = 1000
r = 0.05
n = 10 

fv = pv * ((1+r) ** n )

print (f'{fv}')



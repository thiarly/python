import numpy as np

# 1. Calculando o Retorno Linear

## Criando vetor de preços com numpy
P = np.array([100,50,90])
print (P)
print()

### Inicializando a variável com zeros
r = np.zeros(3)
print(r)
print()
# Usando a equação (1) para calcular o retorno

r[0] = np.nan
r[1] = (P[1] / P[0] -1 )
r[2] = (P[2] / P[1] -1 )

print(r)
print('****'*12)


# O retorno logarítimo:
R = np.zeros(3)
R[0] = np.nan
R[1] = np.log(P[1] / P[0])
R[2] = np.log(P[2] / P[1])
print (R)
print(''*12)
# retorno linerar para retorno log
print (np.log(1+r))
print('****'*12)
# retorno log para retorno linear
print (np.exp(R)-1)

# Retorno acumulado
## Usando a fórmula (5) com t=2
print('****'*12)
r_acum_p = P[2]/P[0] -1
print(r_acum_p)

# Usando a fórmula, do retorno simples r
print('****'*12)
r_acum = (1+r[1])*(1+r[2])-1
print(r_acum)

# A partir do retorno logarítimo R
print('****'*12)
R_acum = R[1]+R[2]
print(R_acum)

print ('CALCULO DE GASTO PÓS CIRUGIA')
print ()
cont = 0

while True:
    soma = float(input('Digite o valor: R$ '))
    resp = str(input('Quer adicionar mais valor? [S/N]: ')).strip().upper()[0]
    cont = cont + soma
    if  resp in "Nn":
        break
resul = cont

print (f' Valor total R$ {resul:.2f}')


"""
print ('\033[1;96m<<< CUSTO PÓS CIRUGIA DO SEPTO >>>\033[m')
print ()
print ('⬇'*50)
print ()
# DIPIRONA, TRANSAMIM E ANTIBIOTICO
a = 185.76
# SORO
b = 35.94
# DECADRON, CIRINGA, GASES E SORO
c = 66.19
# SORO 
d = 28.35
# SORO
e = 25.35
# SORO 
f = 8.28
# SORO
g = 36.09
# DECADRON, SORO
h = 52.98
# SORO
i = 6.39
# SORO
j = 13.98
# SORO
k = 45.52
# VITAMINA C + DIPIRONA
l = 19
# SORO
m = 14.67
# UMCKAN, SORO
n = 105.51
# ALLEGRA
o = 27.29
# ADIPETP
p = 35.59

# SOMA DE TODOS OS PRODUTOS USADOR NO PÓS CIRUGIA
resultado = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p

print (f'\033[1;92mValor total para o tratamento pós cirugia:\033[m \033[1;31m{resultado}\033[m')
"""
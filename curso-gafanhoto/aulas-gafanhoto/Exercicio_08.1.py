import math 
# from math import ceil -> formas de importar individual
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.3f}'.format(num, raiz))

#Arredonda pra baixo
print ('A raiz de {} é igual a {:.3f}'.format(num, math.floor(raiz)))
#Arredonda pra cima
print ('A raiz de {} é igual a {:.3f}'.format(num, math.ceil(raiz)))




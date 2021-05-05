import numpy as np

# Diferenças entre Listas Python a Numpy Arrays
## Vetorização

lista = [0,1,2,3,4,5]
vetor = (np.array(lista))
"""
print (vetor)
print()
print (lista * 2)
print()
print (vetor * 2) # Vai multiplicar cada número da lista por 2
print()
print (vetor + 1)
"""
## Brodcast


a = np.array([[0,0,0], [10,10,10],[20,20,20],[30,30,30]])
b = np.array([[0,1,2],[0,1,2],[0,1,2],[0,1,2]])

#print (a)
#print()
#print(b)
"""
resultado1 = a + b
print(resultado1)
print()
resultado2 = a + [0,1,2]
print(resultado2)
print()
resultado3 = np.array([[0],[10],[20],[30]]) + [0,1,2]
print(resultado3) 
"""

## Operações Aritimétricas
"""
print(vetor + vetor)
print(vetor - vetor)
print(vetor * vetor)
print(vetor / vetor)
print(1 / vetor)
print(vetor ** 3)
"""
##Universal Array Functions
print(np.sqrt(vetor)) #Raiz quadrada
print()
print((np.exp(vetor))) #Exponencial
print()
print((np.sin(vetor))) #Seno
print()
print((np.log(vetor))) #Logaritimo

 


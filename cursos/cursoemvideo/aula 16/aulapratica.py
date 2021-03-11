"""
lanche = hamburguer, suco, piza, pudim
            0          1    2       3
           -4         -3    -2      -1
----------------------------------------------
 print (lanche [2]) -> 2
 print (lanche [0:2]) -> Vai mostrar, 0 e 1
 print (lanche [1:]) -> 1 até o final, 2 e 3    
 print (lanche [-1]) -> = 3 o ultimo elemento
 print (lanche [1:3]) -> Fatiamento entre: sudo e pizza. ignora pudim
print (lanche [:2]) -> Mostre do inicio até o elemento 2, mas o 2 será ignorado (0, 1)
print (lanche [-2:]) -> = -2 até menos -1 
 ----------------------------------------------
 len (lanche ) =Vai contar quantas variaveis tem dentro de lanche 4

 "AS TUPLAS SÃO IMUTÁVEIS"

lanche = () tupla, [] lista, {} dicionário
"""

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
d = a + b
print (d)   
print (c)
print ((c.count(5))) # Quantas vezes aparecer dentro de C o número 5
print (c.index(5)) # Em qual posição está o número 5
print (c.index(5, 1)) # Em qual posição está o número 5, começando a parti da posição 1

"""
-----------------------------------------------------------------
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
for cont in range(0, len(lanche)):
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')
    #print (cont)

print ('Comi pra caramba!')

print (sorted(lanche))
print (lanche)
------------------------------------------------------------------
"""
"""
---------------------------------------------------------
Pode-se usar dessas duas maneiras o for.

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):   -> Se precisar numerar
    print ('Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):  -> Se precisar numerar
    print(f'Eu vou comer {comida} na posição {pos}')
-----------------------------------------------------------
"""

# Tuplas São imutaveis
# lanche [1] = 'refrigerante'
#print (lanche)

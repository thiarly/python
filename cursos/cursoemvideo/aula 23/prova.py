from time import sleep
"""
pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]]
print(pessoas[2][1])
# Resposta: 25
"""
"""
num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1+n2)
# Resposta: 3, 7, 6, 4
"""

"""
num = [8, 2, 4, 2, 5, 2] 
print (num.count(2))
# Resposta: print(num.count(2))
"""
"""
pontos = ()
pontos =(1, 2, 3, 4, 6, 7, 9, 12, 43, 54, 23, 65, 32, 89, 284, 542, 50, 60)
print(sorted(pontos))
# Resposta: print(sorted(pontos))
"""
"""
num = []
num = [6, 2, 1, 4, 3]
num.sort(reverse=True)
print(num)
# Resposta: num.sort(reverse=True)
"""
"""
num = []
num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)
# Resposta: [2, 3, 8, 4, 6]
"""
"""
val = list(range(1, 5))
print (val)
# Resposta: [1, 2, 3, 4]
"""

print('-'*30)
print('RESULTADO CURSO EM VIDEO (PYTHON)')
print('-'*30)
print()

m1 = 100
m2 = 90
m3 = 100

resultado = (m1 + m2 + m3) / 3

print (f'O aproveitamento dos curso M1, M2 e M3 foi de: \033[032m-------> {resultado:.2f}%\033[m')
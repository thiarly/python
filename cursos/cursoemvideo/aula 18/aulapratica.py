"""
Forma de adicionar na lista:

dados = list()
dados.append('Pedro')


"""
"""
dados = list()
pessoas = list()

dados.append('Pedro')
dados.append(25)
pessoas.append(dados[:])

print(dados[0])
print(dados[1])
print (dados)
print(pessoas)
"""
"""
galera = [['Thiarly', 30], ['Laila', 33], ['Clara', 1], ['Lucas', 0.5]]
print (galera[3][0])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
"""
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #fazendo uma cópia de dado para galera
    dado.clear() # apagando a lista dado
    
for p in galera:
    if p [1] >=21:
        print (f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maior e {totmen} menores de idade.')
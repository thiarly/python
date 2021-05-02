conversor = 1.64
conversor1 = 0.64

km = float(input('Digite os KMs da corrida: '))
minutos = float(input('Qual foi o tempo da corrida em minutos?: '))

conv = km *  conversor1 + km
pace = minutos / conv
milha = km / conversor
print (f'conv {conv}')
print(f'O pace da corrida foi: {pace:.2f}')
print(f'O pace da corrida foi: {milha:.2f}')



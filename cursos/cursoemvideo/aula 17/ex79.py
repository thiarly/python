"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
números = list()

while True:

   n = int(input(f'Digite um valor: '))
   if n not in números:
       números.append(n) # Adicionar os valores digitados em N na lista números.
       print ('Valor adicionado com sucesso!')
   else:
       print ('\033[1;31mValor duplicado, insira outro número.\033[m')

   r = str(input('Quer continuar [S/N]')).strip().upper()
   if r in "Nn":
       break 
números.sort() # Ordenar os números em ordem CRESCENTE.
print (f'Você digitou os números: \033[33m{números}\033[m')
   
  
  
"""
  if c == 0:
       maior = menor = listanum[c]
   else:
       if listanum[c] > maior:
           maior = listanum[c]
       if listanum[c] < menor:
           menor = listanum[c]
        
    
print ('-'*30)
print (f'Você digitou os valores {listanum}')

print (f'O maior valor digitado foi {maior} nas posiçãoes ',end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...',end='')
print ()


print (f'O menor valor digitado foi {menor} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end
"""
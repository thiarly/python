# Import Emoji e Sleep  
from time import sleep
import emoji as emoji


# Variaveis de emoji e titulo 

linha = '\033[1;36m - \033[m' * 25
titulo = '#VIVADERENDAPASSIVA'
emo0 = (emoji.emojize(':smiley:' * 35, use_aliases=True))
emo1 = (emoji.emojize(':satisfied:' * 35, use_aliases=True))
emo2 = (emoji.emojize(':small_red_triangle_down:' * 35, use_aliases=True))
emo3 = (emoji.emojize(':small_red_triangle:' * 35, use_aliases=True))

# Print apresentação do programa 

print (emo2)
print ('\033[1;33mCALCULADORA DE JUROS SOBRE CAPITAL PRÓPRIO ( B3 )\033[m')
print (emo3)

# Input: Nome, Empresa e Quantidade

nome = str(input('Digite o seu nome: '))
empresa = str(input('Digite o nome da empresa: '))
quantidade = int(input(f'Digite a quantidade de ações que você possui da empresa {empresa}.: '))

# Variaveis para contador

cont = tot = soma = 0
tot = 0

# While para fazer o calculo e if para critério.

while True:
    jcp = float(input('Qual valor total do JCP a ser pago? R$: '))
    confirma = str(input('Deseja adicionar mais algum JCP? [S/N]: ')).strip().upper()[0]
    
    soma = soma + jcp
    ir = soma * 0.15
    pg = soma - ir
    total = quantidade * pg
    cont = cont + 1

    if confirma in "Nn":
        break

# print com emoji

sleep(2)
print (emo0)
print(titulo.center(74, '-' )) 
print (emo1)

# Print do resultado final 

sleep(1)
if cont <= 1:
    print (f'Valor a ser pago referente a \033[1;33m{cont} JCP.\033[m')
else:
    print(f'Valor a ser pago referente a \033[1;33m{cont} JCPs:\033[m')  

print (f'Valor total do JCP \033[1;31mR$ {soma:.9f}\033[m')
print (f'Valor retido na fonte \033[1;31m15% de IR. R$ {ir:.9f}\033[m')
print (f'Valor liquido a receber por ação da empresa \033[1;34m{empresa}\033[m \033[1;32mR$ {pg:.9f}\033[m')
print (f'\033[1;36m{nome}\033[m, esse é o valor total a receber \033[1;32mR$ {total:.2f}\033[m referente a sua posição em \033[1;34m{empresa}\033[m ')






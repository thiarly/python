"""
Faça um programa que calcule a soma entre todos os números impares que são múltiplos 
de três e que se encontram no intervalo de 1 até 500
"""

soma = 0
cont = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        soma += contagem
        cont += 1

print('\033[34m{}\033[m'.format(contagem))        
print('A soma de todos os \033[31m{}\033[m valores solicitados é \033[32m {}.\033[m'.format(cont, soma))



"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ('Zero','Um','Dois','Três','Quatro','Cinco',
'Seis','Sete','Oito','Nove','Dez','Onze','Doze',
'Treze','Quatorze','Quinze','Dezesseis','Dezessete'
,'Dezoito','Dezenove','Vinte',)


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print ('Número inválido. ', end='')
print (f'Você digitou o número {numeros[num]}')


"""
pos = -1
while pos < 0 or pos > 20:
    pos = int(input('Digite um número entre 0 e 20: '))
    if pos != 0 or pos != 20:
        print ('Número inválido tente novamente.') 
print (f'Você digitou o número: {numeros[pos -1]}')
"""
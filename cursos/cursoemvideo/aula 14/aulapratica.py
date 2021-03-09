"""
While: Quando não se sabe o limite da repetição -> Estrutura de repetição com teste lógico

For: Quando sabe o limite de repetição -> Estrutura de repetição com variável de controle

Ex: Quando se tem um padrão pode usar o For, mas quando não existe padrão o While é a melhor opção.


ENQUANTO NÃO MAÇA:
    se tem chao
        passo
    se tiver buraco
        pula
    se tiver moeda
        pega
pega -> MAÇA :-> Resumindo, o laço será repetido enquanto não pegar a MAÇA

------------------------------------------------------------------------------------

while not MAÇA:
    if chão:
        passo
    if buraco:
        pula:
    if moeda:
        pega
pega

"""
"""for c in range(1, 10):
    print(c, end=' ')
print ('\nFIM')"""

"""c = 1 
while c < 15000:
    print (c)
    c = c + 1
print('FIM!')"""


"""n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print ('FIM!')"""

"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!')"""
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
            print('O número é PAR.')
        else:
            impar = impar + 1
            print('É número é ÍMPAR.')
    else:
        print('FINALIZOU SEM A SOMAS!')

print('ACABOU!')
print ('A soma de todos os números PARES foi {}.'.format(par))
print ('A soma de todos os números ÍMPARES foi {}'.format(impar))








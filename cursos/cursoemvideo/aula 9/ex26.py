
#Faça um programa que leia um frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.


frase = str(input('Digite uma Frase: ')).upper().strip()


print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1)) #O +1 é para n contar a posição 0
print('A Última letra apareceu na posição {}'.format(frase.rfind('A')+1))

#rfind -> começa a procurar a letra a parti do lado direto
#find -> começa a procurar a letra do lado esquerdo
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))

m = (n1 + n2) / 2


print ('Sua média é: {:.1f}'.format(m))

if m >= 7:
    print('Aprovado, boas férias!')
elif m <= 3:
    print ('Necessário refazer a máteria novamente! ')
else:
    print ('Reprovado, é necessário fazer a recuperação! ')

# Condição simplificada:
# print ('Parabéns! if m >=6 else 'Estude Mais!')





#################################################################################################
#nome = str(input('Qual é o seu nome? '))
#if nome == 'Clara':
 #   print ('Que nome lindo você tem! ')
#else:
 #   print ('Que nome normal você tem {}.'.format(nome))



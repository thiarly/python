#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n = str(input('Digite seu nome: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print ('{}!'.format(n))

if m <= 5:
    print ('Essa é a média da sua nota {}. Reprovador! Necessário refazer o ano letivo!'.format(m))
elif m <= 6.9:
    print ('Essa é a média da sua nota {}. Recuperação! Necessário refazer a prova.'.format(m))
else:
    print('Essa é a média da sua nota {}. Parabéns Aprovado! Boas Férias.'.format(m))


    
import emoji as emoji
nome = str(input('Digite o seu nome: '))
prova = str(input('Digite o nome da prova: '))
distancia = float(input('Digite a distancia da natação: '))
horas = int(input('Digite as horas da natação: '))
minutos = float(input('Digite os minutos da natação: ' ))
segundos = float(input('Digite os segundos da natação: '))

#mais = 45
seg = 60
div = 100
formula = 59.826

soma0 = horas * seg
hormin = soma0 + minutos
soma1 = hormin * seg + segundos
soma2 = distancia / div
soma3 = soma1 / soma2
soma4 = soma3 / formula

#print ('Resultado em segundos: {}'.format(soma1))
#print ('Quantidade de passagens por 100m: {}'.format(soma2))
#print ('Total de segundos por passagem AC 100m: {}'.format(soma3))
print ('Parabéns por fazer a prova do {}, {}!'.format(prova, nome))
print ('Tempo: {:.2f}/100m'.format(soma4))
print (emoji.emojize(':smiley: :smiling_imp:', use_aliases=True))








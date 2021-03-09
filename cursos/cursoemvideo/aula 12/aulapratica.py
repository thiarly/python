#Condições anianhadas

nome =float(input('Qual o seu nome? '))

if nome == 'Gustavo':
    print ('Que nome bonito, {}!.'.format(nome))

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil.')

elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal.')

print('Tenha um boa noite, {}!'.format(nome))


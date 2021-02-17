nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo: '))
idade = int(input('Digite sua idade: '))

age = 18

if age < 12:
    print('Você é criança, {}'.format(nome))
    print('Sexo: {}'.format(sexo))
elif age < 18:
    print('Você é adolecente, {}'.format(nome))
    print('Sexo: {}'.format(sexo))
elif age < 60:
    print ('Você é adulto, {}'.format(nome))
    print('Sexo: {}'.format(sexo))
else:
    print ('Você é idoso, {}'.format(nome))
    print('Sexo: {}'.format(sexo))




# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

nome = str(input('Digite o seu nome: '))
dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês de nascimento: '))
ano = int(input('Digite o seu ano de nascimento: '))

print('Olá, {}!'.format(nome))
print('Data de Nascimento, {}-{}-{},'.format(dia, mes, ano))














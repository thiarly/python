#Desenvolva uma lógica que leia peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 a 40: obesidade
# acima de 40: obesidade mórbida



nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o seu Sexo: '))
peso = float(input('Qual o seu peso atual: (Kg) '))
altura = float(input('Digite a sua altura: (m)'))

imc = peso / (altura ** 2)

#################################################
#c = peso / d
#print (d)
#print (c)
# indice de massa corporal
#################################################


print ('Nome: {}.'.format(nome))
print ('Sexo: {}.'.format(sexo))
print ('Peso: {}.'.format(peso))
print ('Altura: {}.'.format(altura))

if imc <= 18.5:
    print('Resultado do IMC {:.1f}, MAGREZA - GRAU 0. '.format(imc))
elif imc <= 24.9:
    print('Resultado do IMC {:.1f}, NORMAL - GRAU 0. '.format(imc))
elif imc <= 29.9:
    print('Resultado do IMC {:.1f}, SOBREPESO - GRAU I. '.format(imc))
elif imc <= 39.9:
    print('Resultado do IMC {:.1f}, OBESIDADE - GRAU II.'.format(imc))
elif imc <= 40:
    print('Resultado do IMC {:.1f}, OBESIDADE GRAVE - GRAU III. '.format(imc))





#Menor que 16 – Magreza grave

#16 a menor que 17 – Magreza moderada

#17 a menor que 18,5 – Magreza leve

#18,5 a menor que 25 – Saudável

#25 a menor que 30 – Sobrepeso

#30 a menor que 35 – Obesidade Grau I

#35 a menor que 40 – Obesidade Grau II (considerada severa)

#Maior que 40 – Obesidade Grau III (considerada mórbida)

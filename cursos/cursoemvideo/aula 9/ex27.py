#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#EX: Ana Maria de Souza
#primeiro: Ana
#ultimo: Souza


nome = str(input('Digite seu nome: ')).strip()

print ('Muito prazer em te conhecer! {}'.format(nome))

lista = nome.split()


print ('O seu primeiro nome é {}'.format(lista [0]))
print ('O seu ultimo sobre nome é {}'.format(lista[len(lista)-1]))




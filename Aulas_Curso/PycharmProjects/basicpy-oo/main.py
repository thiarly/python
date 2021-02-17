from veiculo import Veiculo

caminhao_rosa = Veiculo ('rosa', 6, 'ford', 10)

print('CAMINHAO ROSA')
print ('Cor:', caminhao_rosa.cor)
print ('Marca:', caminhao_rosa.marca)
print ('Tanque:', caminhao_rosa.tanque)

carro_azul = Veiculo ('azul', 4, 'bmw', 30)

print('')
print ('Cor:', carro_azul.cor)
print ('Marca:', carro_azul.marca)
print ('Tanque:', carro_azul.tanque)
carro_azul.abastecer(35)
print ('Tanque:', carro_azul.tanque)
carro_azul.abastecer(70)
print ('Tanque:', carro_azul.tanque)







'''
EXERCICIO: Crie um software de gerenciamento bancário esse software poderá ser capaz de criar clientes e contas
cada cliente possui nome, cpf, idade, cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.
'''
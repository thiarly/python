"""
Dentro do pacote utilidadeCev que criamos no desafio 111, temos um módulo chamado dados. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(), mas com uma validação de dado para aceitar apenas valores que sejam monetários.
"""
from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 40, 60)

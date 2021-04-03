import moeda

p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print (f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print (f'Aumento o {p} em 10% {moeda.aumentar(p, 10)}')
print (f'O desconto de 10% em R$ {p} é R$ {moeda.diminuir(p, 10)}')

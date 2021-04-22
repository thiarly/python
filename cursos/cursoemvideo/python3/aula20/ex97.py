"""
Exercício Python 097 - Um print especia
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def escreva (msg):
    tam = len(msg) + 4
    print ('˜' * tam)
    print (f'  {msg}')
    print ('˜' * tam)


#programa principal
escreva ('Canudos Bahia')
escreva ('Kona 2023 Triathlon')
escreva ('Ironman Brasil 2022')
escreva ('Bike')
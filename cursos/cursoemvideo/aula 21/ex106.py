"""
Faça um mini-sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""

def ajuda (com):
    help(com)

#Programa principal
comando = ''
while True:
    comando = str(input(input("Função ou Biblioteca > ")))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

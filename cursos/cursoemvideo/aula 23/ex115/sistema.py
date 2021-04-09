"""
Crie um pequeno sistema modularizado que permita cadastrar pelo seu nome e idade em uma arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from interface import lib
from interface import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = lib.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        lib.cabeçalho('Opção 2: ')
    elif resposta == 3:
        lib.cabeçalho('Opção 3: ')
        lib.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m ')
    sleep(2)





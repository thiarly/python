"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""

import urllib
import urllib.request

try:
    pudim = urllib.request.urlopen('http://www.pudim.com.br')
    inter = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print(f'O site Pudim não está acessível no momento.')
    print(f'O site Google não está acessível no momento.')
else:
    print(f'Consegui acessar o site Pudim com sucesso.')
    print(f'Consegui acessar o site Google com sucesso.')
    #print (site.read())
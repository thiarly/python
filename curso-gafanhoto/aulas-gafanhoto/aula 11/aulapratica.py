#\033[m
#\033[style;text;backm
#\033[0;33;44m
#STYLE: 0 NOME, 1 BOLD, 4 UNDERLINE, 7 NEGATIVE
#TEXT: 30 BRANCO, 31 VERME, 32 VERDE, 33 AMARE, 34 AZUL, 35 ROXO, 36 AZUL CLARO, 37 CINZA
#BACK: 40 BRANCO, 41 VERME, 42 VERDE, 43 AMARE, 44 AZUL, 45 ROXO, 46 AZUL CLARO, 47 CINZA

# EXEMPLOS:
#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m


#print ('\033[0;30;42mOlá, Mundo!\033[m')

#a = 3
#b = 5
#print('Os Valores são \033[34m{}\033[m e \033[32m{}\033[m'.format(a, b))

n = 'thiarly'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], n, cores['limpa']))
# 
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', n,'\033[m'))
###
# Aula iniciada e finalizada 16/02/201
###


frase= 'Curso em Video em Python'
print(frase[3])
print(frase[3:13])
print (frase[13:])
print (frase[:13])
print (frase[1:12:2])
print (frase.count('o'))
print (frase.find('deo'))
print (frase.lower())
print (frase.replace('Python', 'Android'), frase.upper(), frase.count('o'), frase.split())
print(frase.lower().find('video'))
print(frase.split())
print ('Curso' in frase)
print ('em' in frase)
print ('Testanto123' in frase)


# Subscrevendo a variável, para alterar o Python para 4LINUX.
frase1 = 'Curso em Video em Pytho'
frase1 = frase.replace('Python', '4LINUX')
print (frase1)





#("""len(frase) -> Quantas letras
#frase.count('o') -> quantas letras o
#frase.find('deo') -> vai mostrar em qual posição tem a frase deo
#frase.find('Android') -> Se n tiver a palavra, retorna -1
#'Curso' in frase -> Se tiver a str em frase retorna True se n False
#frase.replace('Python,'Android') -> Substituiria o Python por Android
#frase.upper() -> Alterar de minuscula para maiscula
#frase.lower()-> Vai alterar maiscula para minusculaf
#frase.capitalize()-> Vai modificar todas as letras para minuscula e apenas a 1º letra maiscula
#frase.title()-> Vai alterar para maiscula todos as letras q iniciam as palavras
#Frase.strip() -> Vai remover os espaços inuteis
#Frase.rstrip() -> Vai remover os espaços inuteis da direita
#Frase.lstrip() -> Vai remover os espaços inuteis da esquerda
#frase.split() -> vai transformar uma string em lista
#'-'.join(frase) -> fazer adicionar o - entre as palavras""")
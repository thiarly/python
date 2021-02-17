''''
(Metodo e Função)
EXERCICIO: Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção.
Faça outra função retorne o menor número dessa coleção.
'''

def tem_sete_letras(argumento):
    if len (argumento) == 7:
        return True
    else:
        return False

if tem_sete_letras([1,2,3,4,5,6,7,8]):
    print('realmente tem sete letras')

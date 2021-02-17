"""
Gabriela é uma das professoras do curso de ciência da computação da UFCG e pediu para você fazer uma programa que receba
4 notas e depois, diga se o aluno foi aprovado, reprovado ou terá que fazer uma prova final.

No final, o programa deve imprimir o nome dos alunos que foram aprovados, reprovados e dos que terão que fazer a prova
final.
"""

nome = input('\nNome aluno:')
nota1 = input('Nota prova 1:')
nota2 = input('Nota prova 2:')
nota3 = input('Nota prova 3:')
nota4 = input('Nota prova 4:')

media = int (nota1 + nota2 + nota3 + nota4) / 4.0
if media >= 7:
    print (nome, media, "- Aprovado")
else:
    nota_minima_final = (50 - (media * 6)) / 4.0
    if nota_minima_final > 10:
        print(nome, media, "-Reprovado")
    else:
        print(nome, media, "-Final")

        
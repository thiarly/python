"""
- Erros
- Execões
- Tratamentos

try:
    operação
except:
    falhou
else: 
    deu certo
finally:
    certo/falha
"""





try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

#except Exception as erro:
#    print (f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    ('Tivemos um problam com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiou não informar os dados e saiu.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print (f'O resultado é {r}')
finally:
    print (f'Volte sempre! Muito obrigado.')


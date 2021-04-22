conversor = 1.69

print('-'*55)
print('Oque deseja converter?')
print('-'*55)

print()
print ('opção 1: MILHA -> KM ')
print()

print()
print ('opção 2: KM -> MILHA ')
print()

entrada = int(input('Digite sua opção: ' ))

if entrada == 1:
    mls = float(input('Milhas: '))
    kms = mls * conversor
    print (f'{mls:.2f} milhas são iguais a {round(kms,2)} quilômetros.')

else:
    kms = float(input('Quilometros: '))
    milhas = kms / conversor
    print (f'{kms:.2f} KM são iguais a {round(milhas,2)} Milhas.')


"""
s = float(input('Digite o seu salário: '))

if s >= 1250:
    s1 = (s + (s * 10) / 100  )
    print ('O seu novo salário com reajuste de 10% ficou R$ {}'.format(s1))
else:
    s1 = (s + (s * 15 ) / 100 )
    print('O seu novo salário com reajuste de 15% ficou R$ {}'.format(s1))
"""

"""
mls = float(input('Milhas: '))
kms = mls * conversor
print (f'{mls:.2f} milhas são iguais a {round(kms,2)} quilômetros.')

kms = float(input('Inseir os quilometros: '))
milhas = kms / conversor
print (f'{kms:.2f} KM são iguais a {round(milhas,2)} Milhas.')
"""


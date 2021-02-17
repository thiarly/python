#Criar um sistema que divida em % cada categória de ativo:

acoes = float(input('Digite o valor em ações: '))
fiis = float(input('Digite o valor em Fiis: '))
tesouro = float(input('Digite o valor do Tesouro: '))
cdb = float(input('Digite o valor do CDB: '))
nubank = float(input('Digite o valor em Nubank: '))

patrimonio_total = acoes + fiis + tesouro + cdb + nubank
s = 100

s1 = acoes / patrimonio_total * s
s2 = fiis / patrimonio_total * s
s3 = tesouro / patrimonio_total * s
s4 = cdb / patrimonio_total * s
s5 = nubank / patrimonio_total * s

print ('Patrimônio total: {}'.format(patrimonio_total))
print ('Patrimônio atual em Ações: {:.1f}'.format(s1))
print ('Patrimônio atual em Fiis: {}'.format(s2))
print ('Patrimônio atual em Tesouro: {}'.format(s3))
print ('Patrimônio atual em CDB: {}'.format(s4))
print ('Patrimônio atual em Nubank: {}'.format(s5))




#Criar um programa para medir o m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

resultado = largura * altura
tinha = resultado / 2

print ('Sua parede tem a dimensão de {}x{} e sua área total é de {:.3f}m².'.format(largura, altura, resultado))
print ('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(tinha))


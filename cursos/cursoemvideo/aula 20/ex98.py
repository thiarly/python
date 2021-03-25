from time import sleep

def contador (i, f, p):
    print ('-=-'*20)
    print (f'Contagem de {i} até {f} de {p} em {p}')
    sleep (1)

    if p < 0: 
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i 
        while cont <=f:
            print (f'{cont}',end=' ', flush=True)
            sleep(0.2)
            cont += p
        print ('FIM')
    else:
        cont = i
        while cont >=f:
            print(f'{cont}',end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print ('FIM')
    

contador (0, 100, 10)
contador (100, 0, 10)
print ('-=-'*20)
print ('Agora é sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

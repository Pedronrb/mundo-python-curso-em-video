from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print("Fim")
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é a sua vez de personalizar a contagem!!')
print('=-=' * 20)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inicio, fim, pas)
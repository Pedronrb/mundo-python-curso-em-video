from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=-' * 30)
    print(f'\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print((f'Foram informaados {cont} valores ao todo.'))
    print(f'O maior valor informado foi {maior}')
    print('-=-' * 30)
    
# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
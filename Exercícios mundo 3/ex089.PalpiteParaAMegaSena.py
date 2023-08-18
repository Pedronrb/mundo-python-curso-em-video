from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=-' * 30)
print('     PALPITA DA MEGA SENA     ')
print('-=-' * 30)

quant = int(input('Quantos jogos deseja que eu sorteie? '))
total = 1

while total <= quant:
    cont = 0
    
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1

    lista.sort()
    jogos.append(lista[:]) #Lembrando que "[:]" é para fazer uma CÓPIA.
    lista.clear() #Limpar a lista
    total += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3) 

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('-=' * 3, f' <Boa sorte!> ', '-=' * 3)        

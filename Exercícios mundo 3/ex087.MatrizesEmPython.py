matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3): #Esse for é para colocar os valores na matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
print('-=-' * 30)
for l in range(0,3): #Esse for é para mostrar na tela 
    for c in range(0,3):
        print(f'[{matriz [l] [c]:^5}]', end='')
    print()
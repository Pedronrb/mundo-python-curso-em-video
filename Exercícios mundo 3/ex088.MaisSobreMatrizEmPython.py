matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = maior = somaColuna = 0

for l in range(0,3): #Esse for é para colocar os valores na matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))

print('-=-' * 30)

for l in range(0,3): #Esse for é para mostrar na tela 
    for c in range(0,3):
        print(f'[{matriz [l] [c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()

print('-=-' * 30)
print(f'A soma dos valores pares é: {somaPares}')

for l in range(0, 3):
        somaColuna += matriz[l][2]
print(f'A soma dos valores da terceira colunas é: {somaColuna}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')        




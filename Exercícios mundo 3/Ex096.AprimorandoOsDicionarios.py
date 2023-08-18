times = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c  in range(0, tot):
        partidas.append(int(input(f'   Quando gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas) #sum function for somar.
    times.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in "SN":
            break
        print('Erro!! Responda S ou N. ')
    if resp == 'N':
        break
print('-=' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(times):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'Erro! Não existe o jogador')

    else:
        print(f' -- LEVANTAMENTO DO JOGADORE {times[busca] ["nome"]}: ')
        for i, g in enumerate(times[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
        print('-='*40)
print('   Volte sempre   ')

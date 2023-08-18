def ficha(jog="Desconhecido", gol=0):
    print(f'O jogador {jog} frz {gol} gols')

n = str(input("Nome do jogador? "))
g = str(input("Quantos gols foi feitos? "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
import moeda
p = float(input('Digite um valor R$: '))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}', end="\n")
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
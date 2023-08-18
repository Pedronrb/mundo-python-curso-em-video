import moeda
p = float(input('Digite um valor R$: '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p)}', end="\n")
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
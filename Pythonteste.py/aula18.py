teste = list()
teste.append('Pedro')
teste.append(23)

galera = list()
galera.append(teste[:]) # [:] é para fazer uma cópia e acabar com a ligação q  tem

teste[0] = 'Mariana'
teste[1] = 26
galera.append(teste[:])
 
print(galera)
print(galera[0][1])
print(f'\n')
print('Controle da lista com for: ')
print('Índice 0, nomes: ')
for p in galera:
    print(p[0])
print('Índice 1, idade: ')
for p in galera:
    print(p[1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 334.90)
#OBS se printar o 'n' do 'for', irá colocar em linhas
print('-' * 40)
print(f'{"LISTAGEM DE PRPEÇOS":.^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    #Par é o nome do produto
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    #Objeto
    else:
        print(f'{listagem[pos]:>10.2f}')
print('-' * 40)

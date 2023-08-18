def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno é {largura} X {comprimento} é de {a}m².')

#Programa principal 
print('=-=' * 20)
print('Controle do terreno')
print('=-=' * 20)
print()
l = float(input('Digite a largura em m: '))
c = float(input('Digite o comprimento em m: '))
area(l, c)
print()
print('=-=' * 20)
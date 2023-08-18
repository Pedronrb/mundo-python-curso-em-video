from time import sleep

c = ('\033[m',        # 0 - sem cores  
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - VERDE
     '\033[0;30;43m', # 3 - AMARELO
     '\033[0;30;44m', # 4 - AZUL
     '\033[0;30;45m', # 5 - ROXO
     '\033[7;30m'   # 6 - Branco
     )


def ajuda(com):
    titulo(f'Acessando o manul de comando \'{com}\'', 1)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg} ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#Programa principal:

comando = ''

while True:
    titulo('Sistema de ajuda PyHelp', 3)
    comando = str(input("Função biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!!', 2)
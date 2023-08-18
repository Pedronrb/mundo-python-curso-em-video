def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelio usuário')
            return 0
        else:
            return n

def leiaFloat (msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO!! por favor digite um número real válido.')
            continue
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return n     

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
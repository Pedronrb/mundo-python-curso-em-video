tot18 = 0
totM = 0
totF20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totF20 += 1 

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos é: {tot18}')
print(f'Ao todo temos {totM} de homens cadastrados')
print(f'E temos {totF20} de mulher com mais de 20 anos')
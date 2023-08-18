aluno = dict() #Ou com "= {}" discionário  
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=-' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
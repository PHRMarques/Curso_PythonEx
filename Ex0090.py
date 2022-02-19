""" Faça um programa que leia nome e média de  um aluno, guardando também a situação
em um dicionário. No final, mostre o conteudo da estrutura na tela."""
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('¨' * 60)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')

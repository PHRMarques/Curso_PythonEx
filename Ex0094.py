"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
 os daddos de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final mostre: A) quantas pessoas cadastradas. B) A média de idade. C) uma
 lista com mulheres. D) Uma lista com idade acima da média."""
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M / F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M/F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print("Erro! Responda apenas S ou N.")
    if resp == 'N':
        break
print('\033[32m~=\033[m' * 30)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos. ")
print("C) As mulheres cadastradas foram: ", end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista das pessoas com a idade acima de média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('  <<<<ENCERADO>>>>  ')

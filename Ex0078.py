"""Faça um programa que leia 5 valores numéricos e guarde-os em
 uma lista. No final, mostre qual foi o maior e o menor valor
 digitado e as suas respectivas posições na lista."""
# modo antigo:
"""num = [int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: '))]
print(num)"""
# ou
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'O valor para a posição {c}, será:  ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('\033[31m~=\033[m' * 30)
print(f'Você digitou os valores \033[34m{listanum}\033[m')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f'\033[34m{i}\033[m...', end='')
print()
print(f'O menor valor digitado foi {men} nas posicões ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'\033[34m{i}\033[m...', end='')

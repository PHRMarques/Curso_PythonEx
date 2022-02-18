""" Crie um programa que crie uma matriz de dimensão 3X3 e preencha com
valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [\033[32m{linha}.{coluna}\033[m]: '))
print('\033[31m~-\033[m' * 11)
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'\033[35m[{matriz[linha][coluna]:^5}]\033[m', end='')
    print()
print('\033[31m~-\033[m' * 11)


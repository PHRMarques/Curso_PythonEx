""" Aprimore o desafio 86, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ispar = mai = iscol =  0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [\033[32m{linha}.{coluna}\033[m]: '))
print('\033[31m~-\033[m' * 11)
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'\033[35m[{matriz[linha][coluna]:^5}]\033[m', end='')
        if matriz[linha][coluna] % 2 == 0:
            ispar += matriz[linha][coluna]
    print()
print('\033[31m~-\033[m' * 11)
print(f'A soma dos valores pares é {ispar}')
for  linha in range(0, 3):
    iscol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {iscol}')
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}.')
# Crie um programa que vai gerar cinco números aleartórios e colocar em uma tupla.
# Depois mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'\033[31m{n}\033[m',end=' ')
print(f'\nO maior valor sorteado foi \033[32m{max(numeros)}\033[m')
print(f'O menor valor sorteado foi \033[36m{min(numeros)}')

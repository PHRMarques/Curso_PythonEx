"""Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
  entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
lista = []
jogos = []
print('\033[32m=~\033[m' * 18)
print('           \033[42mJOGA NA MEGA SENA\033[m        ')
print('\033[32m=~\033[m' * 18)
quant = int(input('Você quer sortear quantos jogos? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('\033[32m=~\033[m' * 18)
print('\033[32m=~\033[m' * 3, f'   SORTEANDO {quant} JOGOS  ', '\033[32m=~\033[m' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: \033[36m{l}\033[m')
    sleep(0.5)
print('\033[32m=~\033[m' * 18)
print('Boa sorte')


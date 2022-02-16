"""Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores impares digitados, respectivamente.
Ao final, mostre o conteudo das três listas geradas."""
num = []
pares = []
ímpares =[]
while True:
    num.append(int(input("digite seu número:")))
    resp = str(input('Quer continar? S/N  :'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print("\033[33m=||\033[m" * 25)
print(f'A lista completa de numeros é : {num}')
print(f'A lista de números\033[31m pares\033[m é: {pares}')
print(f'A lista completa de\033[31m ímpares\033[m é: {ímpares}')

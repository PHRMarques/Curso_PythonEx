""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
no final, mostre:
a) Quantas vezes apareceu o numero 9.
b) Em que posicao foi digitado o primeiro valor 3.
c) Quais foram os numeros pares?"""
num = (int(input('Digite o 1 numero: ')),
       int(input('Digite o 2 numero: ')),
       int(input('Digite o 3 numero: ')),
       int(input('Digite o 4 numero: ')))
print(f'Você digitou os valores {num}')
print(f"O valor \033[31m9\033[m apareceu {num.count(9)} vezez(s).")
if 3 in num:
    print(f'O valor 3 apareceu na \033[36m{num.index(3)+1}\033[m posicão')
else:
    print('O valor 3 não foi digitado em nenhuma posicão.')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



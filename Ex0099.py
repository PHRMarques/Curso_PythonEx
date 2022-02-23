"""Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior"""


def maior(* num):
    cont = maior = 0
    print('~=' * 15)
    print('Analisando valores....')
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(1, 2, 6, 0, 3)
maior(1, 0, 999, 4)
maior(1, 2)
maior(0)
maior()

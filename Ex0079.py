""" Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente."""
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não adicionado.')
    r = str(input('Quer adicionar outro? S/N : '))
    if r in 'Nn':
        break
print('\033[36m=||\033[m' * 20)
numeros.sort()
print(f'Você digitou os valores \033[31m{numeros}\033[m.')

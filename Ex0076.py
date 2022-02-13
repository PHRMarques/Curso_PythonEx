"""Crie um programa que tenha uma tupla única com nomes de produtos e seus repectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular."""
listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor',4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('\033[32m~-\033[m' * 25)
print(f'{"Listagem de Preços":^50}')
print('\033[32m~-\033[m' * 25)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('\033[31m~-\033[m' * 25)
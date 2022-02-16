"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção(sem usar o comando sort().
 Mostre a lista ordenada na tela. """
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicão {pos} da lista...')
                break
            pos += 1
print('\033[31m|-=-\033[m' * 20 )
print(f'Os valores digitados em ordem foram \033[36m{lista}\033[m')
""" Crie um programa que tenha uma tupla com várias palavras
(não usar acento). Depois disso, você deve mostrar, para cada palavra,
 quais eram as vogais"""
palavras = ('um', 'dois', 'tres', 'quatro', )
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

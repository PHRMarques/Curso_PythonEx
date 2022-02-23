"""Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""


def escreva(msg):
    tam = len(msg) + 4
    print('\033[32m=\033[m' * tam)
    print(f'  \033[34m{msg}\033[m')
    print('\033[32m=\033[m' * tam)


escreva('Curso em video')
escreva('Paulo Henrique Rodrigues Marques')

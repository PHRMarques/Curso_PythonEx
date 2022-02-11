# Crie um programa que tenha uma tupla totalmente preenchida com a contagem por extenso,de zero ate vinte.
# Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostra-lo por extenso.
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', \
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', \
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero de zero a vinte: '))
    if 0 <= num <= 20:
        break
    print('Tente de novo.  ',end='')
print(f'Você digitou {num}, por extenso ele é {cont[num]}')



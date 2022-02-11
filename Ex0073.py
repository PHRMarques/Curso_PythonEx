"""Crie um tupla preenchida com os 20 primeiros colocados da tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. depois mostre:
A) Os 5 primeiros colocados:
B) Os 4 ultimos colocados:
c) Times em ordem alfabetica:
D) Em que colocação esta o time da Ceará."""

times = ('Chapecoense', 'Atlético', 'Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
       'Bragantino', 'Fluminense', 'America', 'Atlético', 'Santos', 'Ceará', 'Internacional',
       'São Paulo', 'Athletico', 'Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport')
print('\033[37m~~=\033[m' *40)
print(f'Os times do Campeonato sao: \033[34m{times}\033[m')
print('~~=' *40)
print(f'Os 5 primeiros colocados: \033[35m{times[0:5]}\033[m')
print('~~='* 40)
print(f'Os 4 ultimos colocados: \033[30m{times[-4:]}\033[m')
print('~~=' * 40)
print(f'Times em ordem alfabetica: \033[33m{sorted(times)}\033[m')
print('~~=' *40)
print(f'O time do Ceará esta na \033[36m{times.index("Ceará") +1}\033[m posição.')


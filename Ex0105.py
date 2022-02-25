"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
 e vai retornar um dicionário com as seguintes informações:
 – Quantidade de notas
 – A maior nota
 – A menor nota
 – A média da turma
 – A situação (opcional)"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita  várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar  a situação
    :return: Dicionário com várias informções sobre a situação do turma.
    """

    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)

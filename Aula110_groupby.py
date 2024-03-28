
# groupby - agrupando 

from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

from Aula109_Combinations_permutations_product import print_iter

lista_alunos_ordenados = [
    {**aluno, "nome": aluno["nome"]} 
    for aluno in sorted(alunos, key=lambda x: x["nota"])
]


grupos = groupby (lista_alunos_ordenados,key=lambda x: x["nota"] )
# O groupy necessita ser ordenado
# Usar sorted

for chave, grupo in grupos:
    print (chave)
    print_iter (list(grupo))


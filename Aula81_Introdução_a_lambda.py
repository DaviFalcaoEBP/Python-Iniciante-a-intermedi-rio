
# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

'''lista = [4, 32, 1, 34, 5 ,6,6,21]

lista.sort( reverse = True )
print (lista)'''


'''lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir (lista):
    for item in lista:
        print (item)
    print ()

l1 = sorted (lista, key= lambda item: item ["sobrenome"])

exibir (l1)
'''









'''
def exibir (lista):
    for item in lista:
        print (item)
    print ()

l1 = sorted(lista, key = lambda item: item['nome'])
l2 = sorted(lista, key = lambda item: item['sobrenome'])

exibir (l1)
exibir (l2)
'''















# Função lambda é um modo de utilização de funções anônims

# Lista de dicionários
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Função explícita para ordenar valores
def exibir_ordem(chave):
    # Criação de uma variável contendo uma nova lista baseada na ordenação da original
    lista_ordenada = sorted(lista, key=lambda x: x[chave])
    # Print da lista ordenada
    print(lista_ordenada)

# Uso da função explícita com a chave "nome"
exibir_ordem("nome")

# Uso da função explícita com a chave "sobrenome"
exibir_ordem("sobrenome")

# Forma de fazer com criação de função implícita para ordenar valores
lista_ordenada_impl = sorted(lista, key=lambda x: x["nome"])
print(lista_ordenada_impl)

# Uso deste print (print (help(sorted))) pode ajudar a entender quais são os requisitos do comando sorted, que são:
# 1. Uma iterável: a lista 
# 2. A chave como argumento nomeado 
# 3. A função implicita lambda, o qual a pede um argumento e uma expressão, no caso qual o fator utilizado para organizar a lista




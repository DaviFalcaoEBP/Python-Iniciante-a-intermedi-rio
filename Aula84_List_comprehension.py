
# List comprehesion em Python
# List comprehesion é um forma rápida para criar listas
# a partir de iterávies

#print (list(range(10)))

import pprint

# Criação de uma função para deixar o print mais customizado
def p(v):
    pprint.pprint (v, sort_dicts=False, width= 40)

# Criação de uma lista vazia
lista = []
# Forma normal de iterar sobre uma lista, no sentido de adicionar por iteração ate o range 10 usando .append
for numero in range (10):
    lista.append (numero)
print (lista)

# Realização de um compreensão dentro da lista, ou seja, uma iteração em seu interior
lista = [
    numero * 2
    for numero in range (10)
    ]
print (lista) 


produtos = [
    {"nome": "p1", "preco": 20, },
    {"nome": "p2", "preco": 10, },
    {"nome": "p3", "preco": 30, },
]

produtos = [
    {"nome": "p1", "preco": 20, },
    {"nome": "p2", "preco": 10, },
    {"nome": "p3", "preco": 30, },
]

novos_produtos =  [
    # Desempacotamento do dicionário criado com todas as chaves e valores
    # Apresentação do argumento "preco" e expressão a ser aplicada
    {**produto, "preco": produto["preco"] * 1.05}
    # Condicional para determinar o novo dicionário criado
    if produto['preco'] > 21 else {**produto}
    # Iteração com for para criar uma lista de produtos baseada na verificação de toda a lista de produtos
    for produto in produtos
]

novos_produtos1 = [
    # Somente desempacotamento da lista nova produto1
    {**produto1}
    # Criação da lista nova produto1
    for produto1 in produtos
]

print (novos_produtos1)




'''novos_produtos = [
    {**produto, "preco": produto["preco"]*1.05}
    if produto ["preco"] > 20 else {** produto}
    for produto in produtos
        if produto ["preco"] > 10
]

print (novos_produtos)
#print (*novos_produtos, sep = '\n')
# p (novos_produtos)

lista = [n for n in range(10) if n< 5]
#print (lista)
'''

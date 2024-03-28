# Combination, Permutations e Product - itertools
# Combinação - ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


# Função interresante para descomprimir listas
def print_iter (iterador):
    print (*list(iterador), sep = '\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ["p", "m", "g"], 
    ["masculino", "feminino", "unisex"],
    ["algodão", "poliéster"]

]

# Atua no sentido de fazer combinações de dados, tendo que decidir o tamanho das combinações
print_iter (combinations(pessoas,2))
print ()
# Atua fazendo permutações de dados, tendo que decidir o tamanho
print_iter (permutations(pessoas,2))
print ()
# Atua fazendo todas as possibilidades de iteração entre dados
print_iter (product(*camisetas))
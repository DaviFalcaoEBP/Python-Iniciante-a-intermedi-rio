
# reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]


'''def funcao_reduce (Acumulador, produto):
    print ("Acumulador", Acumulador)
    print ("produto", produto)
    print ()
    return Acumulador + produto ["preco"]


total = reduce (
    funcao_reduce, 
    produtos,
    0
)'''

total = reduce (
    lambda acu, pro: acu + pro["preco"],
    produtos,
    0
)

print (total)

'''total = 0
for produto in produtos:
    total += produto["preco"]

print(f'{total:.2f}')'''

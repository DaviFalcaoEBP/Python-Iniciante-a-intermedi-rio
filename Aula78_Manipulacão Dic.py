# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


# Importação do módulo copy para utilização de deepcopy
import copy

# Apresentação de um dicionário
d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2]
}

# Deepcopy: Realização de uma cópia profunda do dicionário d1 em todas as camadas (chaves, valores e lista)
# Finalidade de poder modificar o d2 sem afetar o d1
d2 = copy.deepcopy(d1)

# Modificando valores em d2
d2["c1"] = 100
d2["l1"][1] = 9999

# Imprimindo os dois dicionários
print("d1:", d1)
print("d2:", d2)


# Apresentação de um dicionário
p1 = {
    "nome" : "Davi",
    "Sobrenome": "Falcão"
}

# Pega o valor de uma chave para apresentar com o print
print (p1.get("nome", "Davi"))

# Apaga a chave, somente imprimindo o valor
nome = p1.pop ("nome")
print (nome)

# apaga o ultímo item adicionado e depois está mostrando qual item foi 
ultima_chave = p1.popitem()
print(ultima_chave)

# O que sobrou da lista
print (p1)


# Adiciona novos valores ao dicionário

p1.update ({

    "nome": "novo valor",
    "idade": 30
})

# Adiciona novos valores em dicionpario mais o adiciona como tupla
tupla = (("nome", "novo valor"), ("idade", 30))
p1.update (tupla)
print (p1)



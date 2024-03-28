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


pessoa = {
    "Nome": "Davi ",
    "Sobrenome": "Falcão",
    #"idade": 90
}

# len conta quantas chaves existem no dicionário
print (len(pessoa))

# Keys retorna quais são as chaves iteráveis no dicionário
print (pessoa.keys())

# Trasformação do dicionário em uma lista por List e apresentação dos valores do dicionário por values
print (list(pessoa.values()))

# Values retorna de forma iterável as chaves e os valores do dicionário
print (list(pessoa.items()))

# Adição do valor da chave se essa não existir ou modificação da existente
pessoa.setdefault ("idade", None)
print (pessoa["idade"])


'''for valor in pessoa.keys():
    print (valor)'''

# Usando o for para passar por todas as chaves e valores, mostrando eles pela iteração com .items()
for chave, valor in pessoa.items():
    print(chave, valor)
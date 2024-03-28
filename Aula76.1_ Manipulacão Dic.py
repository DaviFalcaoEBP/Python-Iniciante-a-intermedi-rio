# Criação de um dicionário vazio para manipulação
pessoa = {}

# Criação de uma chave com adição de um valor usando uma variável
chave = "nome_completo"
pessoa[chave] = "Davi Falcão"

# Criação de uma segunda chave diretamente no dicionário
pessoa["Sobrenome"] = "Miranda"

# Impressão do dicionário
print(pessoa)

# Impressão somente da chave "nome_completo" do dicionário
print(pessoa[chave])

# Modificação da chave "nome_completo" e remoção da chave "Sobrenome"
pessoa[chave] = "Maria"
del pessoa["Sobrenome"]
print(pessoa)

# Aplicação de get para a checagem da existência da chave "Sobrenome" com condição if
if pessoa.get("Sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["Sobrenome"])
















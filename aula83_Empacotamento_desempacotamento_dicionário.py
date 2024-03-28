
# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

#print (a,b)

pessoa = {
    'nome': 'aline',
    'sobrenome': 'Fernanda'}

# So checar a função de items, atua nas chaves e valores
print (pessoa.items())

# Nessa forma, as variáveis quando colocadas em parenteses em duplas atuam como chave e valor
# Ou seja, ocorre o desempacotamento em tuplas dos valores

(a1, a2), (b1, b2) = pessoa.items ()
print (a1, a2)
print (b1, b2)

# Essa é outra forma de mostrar as chaves e valor porém por meio da iteração interna do for em todos os itens 
# Da lista
for chave, valor in pessoa.items():
    print (chave, valor)

'''--------------------------------------------------------------------------------------------------'''



#Apresentação de uma lista no qual os valores são tipo float e int
dados_pessoa = {
    "idade": 16, 
    "altura": 1.6,
}

# Criação de novos dicionários por meio do desempacotamento de informações (**), e subituição do valor das chaves
pessoa_completa = {**pessoa, "nome": "Fernando"}
Pessoa_dados = {**dados_pessoa, "idade": 19}

print (pessoa_completa)
print (Pessoa_dados)

# Observação pessoal: Eu tentei usar diretamente a função print de forma a desempacotar um dicionário para facilitar a leitura
# Porém isso nãp é permitido, tem que na verdade fazer uma iteração com for

#Método errado
#print (**pessoa)

# Método certo
for chave, valor in pessoa.items():
    print (chave, valor)


"""--------------------------------------------------------------------------------------------------------------"""

# args e kwargs
# args: Atua no empacotamento de dados tipo argumentos não nomeados pu posicionais
# kwargs - keyword arguments (argumentos nomeados)
# Se aplicar os dois, qualquer argumento pode ser aceito


# Criação de uma função externa, que aceita tanto qualquer argumento nomeado quanto não nomeado
def mostro_argumentos_nomeados(*args, **kwargs):
    # Entrada de um print para calcular o número de argumentos não nomeados
    print ("NÃO NOMEADOS:", args)
    # Iteração com for para mostrar, e não calcular, o numero de items nomeados
    for chave, valor in kwargs.items():
        print (chave, valor)

# Demostração de argumentos não nomeados, sendo o 1 e 2
mostro_argumentos_nomeados (1, 2, nome = "Joana", qlq = 123)

# Apresentação de somente argumentos nomeados provindo da lista, sendo argumentos nome = e sobrenome=
mostro_argumentos_nomeados (**pessoa_completa)






# copy, sorted, produtos.sort

# Importação da biblioteca copy
import copy

# Importação de uma pasta de dados
# Obs: Utilização de um thunder init para modulação do arquivo.py como biblioteca
# Importação de somente a lista de produtos
from dados import produtos

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    # Abriu a lista nova, com modificação da estrututa interna de uma variável 
    {**produto, "preco": produto ["preco"] * 1.1}
    # Criou uma lista nova com os itens da lista produtos
    for produto in produtos

]

# Checagem se sem aplicação de deepcopy, ocorre a modificação da lista original se ela vier de um arquivo importado
# Resposta: Não
print (*produtos, sep = '\n')
print ()
print (*novos_produtos, sep = '\n')


#Exercício
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Cria uma lista ordenada no sentido que a iterável antes passa por um deepcopy ( Cópia em todos os níveis)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy (produtos),
    key = lambda p: p['nome']
)

# Checagem da deep copy novamente, utilização de um desempacotador de lista * e também um separador de linha \n
print (*produtos, sep = '\n')
print ()
print (*produtos_ordenados_por_nome, sep = '\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# A diferença entre códigos se deve ao fato que um a lambda tem como indix de ordenação do sorte sendo o preço
produtos_ordenados_por_preco = sorted(
    copy.deepcopy (produtos),
    key = lambda p: p['preco']
)

# Checagem da deepcopy novamente
print (*produtos, sep = '\n')
print ()
print (*produtos_ordenados_por_preco, sep = '\n')



#Dictionary comprehension e Set Comprehension

produto = {
    "Nome": "Caneta Azul",
    "Preco": 2.5,
    "Categoria": "Escritório",
}


dc = {
    chave: valor
    # Aplicação de is isistance, voltand um bollean, que atua para checagem de um objeto (valor) e determinação do tipo
    # Se o objeto valor for um int ou float, seguir o código, se não, colocar em letra maiscula
    if isinstance (valor, (int,float)) else valor.upper()
    # Iteração com for criando um novo dicionário contento tanto as chave como valor do dicionário lista
    for chave, valor in produto.items ()
    if chave == "Categoria"
}


print (dc)

dc1 ={
    # No caso do dicionário, invés de ocorrer o desempacotamento **, ocorre a apresentação de chave: valor do novo dic
    chave: valor
    if isinstance (valor, (int, float)) else valor.upper()
    # Iteração que irá gerar o novo dic que acima irá ser gerado
    for chave, valor in produto.items()
    if chave == 'Categoria'
}

isinstance

print (dc1)
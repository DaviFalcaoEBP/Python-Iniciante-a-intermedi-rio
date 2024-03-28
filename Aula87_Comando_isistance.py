
#isinstace - para saber se objeto é determinado tipo

lista = [
    "a", 1, 1.1, True, [0, 1, 2], 
    (1, 2), {0, 1}, {"nome": "Luiz"}, 
]

for item in lista:
    # Verifica se o item é do tipo set
    if isinstance(item, set):
        print("SET")
        # Adiciona o valor 5 ao conjunto
        item.add(5)
        # Imprime o conjunto modificado e verifica se ainda é uma instância de set
        print(item, isinstance(item, set))

    # Verifica se o item é do tipo string
    if isinstance(item, str):
        print("STR")
        # Imprime a versão em maiúsculas da string
        print(item.upper())

    # Verifica se o item é do tipo int ou float
    if isinstance(item, (int, float)):
        print("NUM")
        # Imprime o item e seu dobro
        print(item, item * 2)
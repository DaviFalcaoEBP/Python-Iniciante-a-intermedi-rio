
# Generator expressiom, Iterables e Iterators em Python



# Primeira aparição de importação de módulo
import sys

# Criação de um lista com strings
iterable = ["Eu", "tenho", "_iter_"]

# Criação de um iterador, com checagem se é iterável
iterator = iterable.__iter__ () # tem _iter_ e _ next_

# Criação de uma lista contendo a iteração de n indo de 0 a 99
# Comparação do consumo de memória considerando que listas necessitam armazenar dados para depois apresentar
lista = [n for n in range (100)]

# Criação de um gerador contendo a iteração de n indo de 0 a 99
# Neste caso os números são gerados sem index e sendo percorridos somente uma vez
generator = (n for n in range (100))

# Comparação entre o tamanho em bytes de armazenamento de um de outro

print (sys.getsizeof(lista)) # Lista: 920 bytes
print (sys.getsizeof(generator)) # Generator: 192 Bytes

# No caso, a utilização da lista é mais adequada para checagem de valores em índices, mas para dados grandes é melhor usar generator

for n in lista:
    print (n)



    
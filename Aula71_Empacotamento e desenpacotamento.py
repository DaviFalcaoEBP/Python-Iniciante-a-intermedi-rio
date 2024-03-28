
"""
args -- Argumentos não nomeados
*-* args ( enpacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# Resto: Enpacotamento


'''x, y, *resto = 1, 2, 3 , 4
print (x , y, resto)'''

'''def soma(x + y):
    return x + y'''

'''def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1,2,3,4,5,6
outra_soma = soma (*numeros)
print (outra_soma)'''



'''soma_1_2_3 = soma (4, 5, 6)
print (soma_1_2_3)

print (sum((1,23)))'''




# Criação da função soma e empacotamento em tupla de argumentos não nomeados
def soma (*args):

# Criação de um contador
    total = 0
# Checagem com For de todos os argumentos desempacotados da tupla com adição
    for numero in args:
        total += numero

# Retorno do contador após todas interações com for
    return total
    
# Definição de uma tupla de números
numeros = 1, 2, 3, 4, 5
# Chamada da função soma, desempacotando a tupla como argumentos
outra_soma = soma(*numeros)
# Impressão do resultado da soma
print(outra_soma)
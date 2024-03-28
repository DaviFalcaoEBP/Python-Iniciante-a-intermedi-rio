
def executa (funcao, *args):
    return funcao (*args)

def Criar_multiplicador (multiplicador):
    return lambda numero: numero * multiplicador

duplica = executa (Criar_multiplicador, 2)

print (duplica(30))













'''
def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    return lambda numero: numero * multiplicador

# Utilizando a função executa para criar uma função que duplica
duplica = executa(criar_multiplicador, 2)

print(duplica(10))'''

# Realização de comparação de soma por meio de 3 métodos
'''print (
    executa (
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma, 2, 3),
    soma (2, 3)
)'''
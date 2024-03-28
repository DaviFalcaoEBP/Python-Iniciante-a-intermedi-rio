
# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
Não nomeados recebidos
Retirne o total para uma variável e mostre o valor 
da variável
"""

def multiplica (*args):
    total_multiplicacao = 1
    for numeros in args:
        total_multiplicacao *= numeros
    return total_multiplicacao
    
Numero = 1, 2, 3, 4,5, 10

resultado = multiplica (*Numero)
print (resultado)

'''def par_impar ():
    if numero %2 == 0:
        return print (f"O número {numero} é par")
    else: 
        return print (f"O número {numero} é impar")

numero = int(input (" Entre com um número: "))
resultado = par_impar()
print (resultado)'''

def par_impar (numero):
    multiplo_de_dois = numero %2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print (par_impar(2))

"""
Higher order functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg

print (saudacao("Bom dia"))

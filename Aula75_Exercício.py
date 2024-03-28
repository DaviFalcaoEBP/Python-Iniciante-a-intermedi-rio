"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""



'''def multiplicador_1 (numero):
    def multiplicador_2 (numero_2):
        int_numero = int(numero_2)
        numero_duplicado = int_numero*2
        return f"O {numero_2} duplicado é {numero_duplicado}"
    return multiplicador_2(numero)

print (multiplicador_1(2))'''
'''
def multiplicador_1 (numero):

    def duplicador (numero_2):
        return f"O {numero_2} duplicado é {numero_2*2}"
    
    def triplicador (numero_3):
        return f"O {numero_3} triplicado é {numero_3*3}"
    
    def quadruplificador (numero_4):
        return f"O {numero_4} quadruplicado é {numero_4*4}"


    return duplicador(numero), triplicador (numero), quadruplificador (numero)


print (multiplicador_1(3))

def criar_multiplicador(mulplicador):
    def multiplicar(numero):
        return numero * mulplicador
        
    return multiplicar

duplicar = criar_multiplicador (2)
triplicar = criar_multiplicador (3)
quadruplicar = criar_multiplicador (4)

print (duplicar(2))
print (triplicar(2))
print (quadruplicar(2))'''




def criar_multiplicar (numero):
    def multiplicador (multiplicador):
        return numero * multiplicador
    return multiplicador

multiplicacao_por_dois = criar_multiplicar (2)


resultado = multiplicacao_por_dois(2)
print (resultado)

# Criando a função multiplicadora como lambda
criar_multiplicar = lambda numero: lambda multiplicador: numero * multiplicador

# Criando uma função específica para multiplicar por 2
multiplicacao_por_dois = criar_multiplicar(2)

# Chamando a função criada
resultado = multiplicacao_por_dois(2)

# Imprimindo o resultado
print(resultado)

# Adiando funções

# Função soma, com apresentação de dois argumentos não nomeados e retorno da soma
def soma (x,y):
    return x + y 

# Função multiplica com dois argumentos e return de multiplicação
def multiplica (x, y):
    return x * y

# Função executa, recebe argumento como sendo a funcao e o primeiro argumento x das outras funcoes
# Atua no sentido que necessita ser definido a funcao, porem essa só sera executada na funcao interna
# Tendo que retorna a funcao interna em closure

def executa (funcao, x):
    def interna (y):
        return funcao (x,y)
    return interna 

# Criação de uma variável no qual
# 1. Executa a função executar, apresentado o argumento funcao e x
multiplica_por_dez = executa (multiplica, 10)

# Print com a apresetnação do argumento y para a função interna
print (multiplica_por_dez(10))

# Objetivo: Adiar a realização de uma função com closure, por meio de apresentação adiada do argumento y
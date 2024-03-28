# Decoradores com parâmetros

# Função que retorna um decorador com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    # O retorno dessa função será o decorador propriamente dito
    def fabrica_de_funcoes(func):
        # Código executado no momento em que o decorador é aplicado
        print('Decoradora 1')

        # Função aninhada que substituirá a função original
        def aninhada(*args, **kwargs):
            # Exibição dos parâmetros do decorador
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            # Chamada da função original e retorno do resultado
            res = func(*args, **kwargs)
            return res

        # Retorna a função aninhada para ser usada como decorador
        return aninhada

    # Retorna o decorador propriamente dito
    return fabrica_de_funcoes


# Aplicação do decorador com parâmetros à função soma
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    # Função original que será substituída pela função aninhada
    return x + y


# Criação de um decorador sem parâmetros
decoradora = fabrica_de_decoradores()

# Criação de uma função decorada usando o decorador sem parâmetros
multiplica = decoradora(lambda x, y: x * y)

# Chamadas das funções decoradas
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)

# Exibição dos resultados
print(dez_mais_cinco)  # Saída: 15
print(dez_vezes_cinco)  # Saída: 50
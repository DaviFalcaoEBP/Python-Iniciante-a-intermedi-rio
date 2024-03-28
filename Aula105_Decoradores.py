
def parametros_decorador (nome):
    def decorador (func):
        print ("Decorador:", nome)
    
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
    
        return sua_nova_funcao
    return decorador

@parametros_decorador (nome = "primeiro")
def soma(x,y):
    return x +y 

dez_mais_cinco = soma (10,5)
print (dez_mais_cinco)















'''A função aninhada em um decorador atua como um wrapper em torno da função original, 
proporcionando uma maneira padronizada de introduzir lógica adicional antes e/ou depois da 
execução da função decorada. Essa abordagem é útil quando você deseja aplicar um comportamento 
comum a várias funções sem ter que repetir o mesmo código em cada uma delas.
'''


def criador_de_funcoes ():
    # Decorador em si
    def interna_decorador(func):
        print ("Checagem do decorador, pré decoração")
        # A função aninhada tem a função de aninhar a função que o decorador está atuando sobre, o decoroando
        # Antes que ocorra a execução
        def aninhada(*args, **kwargs):
            print ("Aninhamento da função")
            resultado = func (*args, **kwargs)
            return resultado
        
        return aninhada
    return interna_decorador


@criador_de_funcoes ()
def soma (x, y):
    return x +y

conta_dois_soma = soma (2,3)

print (conta_dois_soma)


            






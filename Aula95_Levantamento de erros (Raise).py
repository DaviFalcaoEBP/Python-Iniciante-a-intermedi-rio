
# raise -- Lançando exceções (erros)

# Raise é util para levantar erros no programa no sentido de trazer uma mensagem de aviso de o porque a seção
#está errada

# Função não aceita zero: Atua no sentido de que se o denominador for zero

def nao_aceito_zero (d):
    if d == 0:
        # Levantara um erro do tipo ZeroDivisionError por uso de Raise
        raise ZeroDivisionError ("Você esta tentando dividir por zero")


# Função de determinação de tipo: Utilizada no caso de se o valor de entrada como número int ou float
def deve_ser_int_ou_float (n):
     tipo_n = type (n)
     # Utilização de uma condição com checagem por isistance se o valor for um int ou float 
     # Levantamento de um erro do tipo TypeError
     if not isinstance (n, (float, int)):
        raise TypeError (

                f"{n} deve ser in ou float\n"
                f"{tipo_n.__name__} enviado"
        )
     return True
    
# Função executadora das outras funções com argumentos de numerador e denominador para divisão
# Executa tanto para o numerador quanto o denominador para entrada só de int e float
# Executa checagem de divisão por zero usando a função criada não aceita zero

def divide (n,d):
    deve_ser_int_ou_float (n)
    deve_ser_int_ou_float (d)
    nao_aceito_zero (d)
    return n / d


# Passagem de argumentos e impressão
print (divide(8,0))




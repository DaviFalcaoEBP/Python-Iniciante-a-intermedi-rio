
# Try, except, else e finally

'''a = 18
b = 0
c = a/b
'''

# Introdução: Não é comum em sistemas a prática de utilização de somente Except no sistema, devido a passar qualquer
# tipo de erro sem a categorização do mesmo, por isso a definição destes

try:
   a = 18
   b = 0
   print (b[0])
   print ("Linha 1")
   c = a/b
   print ("Linha 2")

except ZeroDivisionError: # Chamado de erro de divisão por zero
    print ("Divisão por zero")
except NameError: # Chamado de falta de definição de uma variável
    print ("Nome B não está definido")
except (TypeError, IndexError) as error: #Classes de erros e "ERROR" se trata de uma variável
    print ("TypeError + IndexError")
    print ("MSG:", error)
    print ("Nome:", error.__class__.__name__) # Apresentação do iterador do erro
except Exception: # Desconhecimento do erro
    print ("Erro não definido")

print ("Continuar")




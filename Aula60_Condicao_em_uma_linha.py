"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
'''condicao = 10 == 11
variavel = "Valor" if False else "Outro valor"
print (variavel)'''

'''digito = 10
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito

print (novo_digito)'''

# Simplificação de linha de código (IMPORTANTE), atua no sentido apresentar de:
# 1. Passo 1: Apresentar a resposta se if for verdadeiro 
# 2. Usar o if com condição direta da variável 
# 3. Apresentação do Else se o boolen voltar false
print ("valor" if True else "Outro valor")



print ("Acertou" if 23 <= 2 else "Errou" )
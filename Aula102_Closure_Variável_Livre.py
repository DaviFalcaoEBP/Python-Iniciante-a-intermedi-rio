
# Variáveis livres + nonLocal (locals, globals)

def fora(x):
    # A é considerado uma variável livre por não estar dentro do escopo da função dentro
    a = x

    def dentro ():
        # Indica quais variáveis são locais com locals
        print (locals())
        return a
    return dentro

dentro = fora (10)

print (dentro())

# A função concatenar nesse caso é util no sentido de que podemos definir funções fora do escopo da função interna
# Porém trabalharmos ela internamente com modificações da mesma

def concatenar(string_inicial):

    # Valor final sendo uma variável livre
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # Aplicação de nonLocal para não considerar como variável local
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

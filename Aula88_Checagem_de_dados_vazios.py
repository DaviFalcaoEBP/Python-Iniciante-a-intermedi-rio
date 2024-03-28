
#Valores Truthy e Falsy, Tipos mutáveis e imutáveis
# Mutáveis [] {} set ()
# Imutáveis () "" 0 0.0 None False range (0,10)

lista = [1,2]
dicionario = {}
conjunto = set ()
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None
Falso = False
intervalo = range (10)

# Comando voltado para a checagem de valores vazios (falsy) ou com dados (truthy)
def falsy(valor):
    return "Falsy" if not valor else "Truthy"

print (f'TESTE', falsy ("TESTE"))

print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{Falso=}', falsy(Falso))
print(f'{intervalo=}', falsy(intervalo))

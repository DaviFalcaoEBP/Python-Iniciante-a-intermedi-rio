
#Yield From

def gen1():
    print ("Começou g1")
    yield 1
    yield 2
    yield 3
    print ("Acabou g1")

def gen3():
    print ("Começou g3")
    yield 10    
    yield 20
    yield 30
    print ("Acabou g3")

def gen2(gen):
    print ("Começou g2")
    yield from gen()
    yield 4
    yield 5
    yield 6
    print ("Acabou g2")

g = gen2(gen1)
g = gen2(gen3)


for numero in g:
    print (numero)


















# Geração de funções geradoras conectadas: Capacidade de utilizar yield from para importar geradores de outras 
# Funções
    
#Criação da primeira função
    
def generator1 ():
    print ("Comecou a g1")
    yield 1
    yield 2
    yield 3
    print ("Acabou a g1")

def generator3 ():
    print ("Começou a g3")
    yield 10
    yield 20
    yield 30
    print ("Acabou a g3")

def generator2(gen):
    print ("Começou g2")
    yield from gen() # Tradução: Função geradora de outro argumento, podendo ser uma função
    yield 4
    yield 5
    yield 6
    print ("Acabou g2")

g = generator2 (generator1) # Argumento gen do generator2 sendo o generator1
g = generator2 (generator3) # Argumento do gen do generator1 sendo o generator2


for numero in g:
    print (numero)











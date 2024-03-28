
# Introdução às Generator fuction em python
# generator = (n for n in range (10000))

# O yield transforma a função de uma gerador que irá interar o argumento e irá pausar

def generator (n = 0):
    yield 1 # Pausar
    print ("Continuando...")
    yield 2 # Pausar
    print ("Continuando...")
    yield 3 # Pausar
    print ("Acabou")
    return "Acabou"

# O next atua no sentido de chamar o próximo o próximo yield até chegar no return que atua como StopInteraction
gen = generator (n=0)
print (next(gen)) # Next para o primeiro valor
print (next(gen)) # Next para o próximo valor
print (next(gen)) # Next para o próximo valor



# Criação de uma função geradora que atua no sentido de criar uma gerador por N in loop, executando no total 10 geradores de número
def generator (n = 0, maximun = 10):
    while True: 
        yield n 
        n +=  1

        if n> maximun:
            return

# Colocação em variável a execução da função
gen = generator ()

# Impressão da função por número demandado e não armazenado
# Atuação do for como Next para que cada yield gerador seja executado
for n in gen:
    print (n)
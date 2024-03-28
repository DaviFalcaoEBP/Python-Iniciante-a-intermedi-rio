
# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes (nome, lista =None):
    if lista is None:
        lista = []
    lista.append (nome)
    return lista

# A lista é continuamente usada nesse caso


cliente1 = adiciona_clientes ("Davi")
adiciona_clientes ("Joana", cliente1)
cliente1.append ("Edu")


cliente2 = adiciona_clientes ("Helena")
adiciona_clientes ("Joana", cliente2)

cliente3 = adiciona_clientes ("Moreira")
adiciona_clientes = ("vivi", cliente3)


print (cliente1)
print (cliente2)
print (cliente3)

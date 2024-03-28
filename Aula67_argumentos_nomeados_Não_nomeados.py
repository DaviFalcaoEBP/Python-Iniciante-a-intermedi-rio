'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''


# Apresentação de argumentos nomeados e não nomeados
# Argumentos nomeados não precisam de ordem para serem chamdados, pois já possui um argumento
# Argumentos não nomeados necessitam de posicionamento, ou seja, a posição de chamada de argumento muda

def soma (x, y, z=None):
    # Criação de uma condição para que se o valor de z não for vazio, acresentar ele na conta, ou não apresentar
    if z is not None:
        print (f"{x= } {y=} {z=} soma:", x+y+z)
    else:
        print (f"{x= } {y=} soma:",x+y)

soma (1,2)
soma (5,3)
soma (100, 200, 0)

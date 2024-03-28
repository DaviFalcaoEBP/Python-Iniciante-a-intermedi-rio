'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''


def soma (x,y,z):
# Definição
    print(f'{x = } + y = {y} + z ={z}',"|"  "x + y + z = ", x + y +z)

# Apresentação de argumentos não nomeados
print (soma(1,2,3))

# Apresentação de argumntos nomeados
print (soma(y=2,z = 3,x=1))

# Aprsentação de argumentos não nomeados, e aplicação de uma separador sep 
print(1, 2, 3, sep = "-")
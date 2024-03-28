'''from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula99_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)'''

'''print (__name__)

from aula99_package.modulo import soma_do_modulo, fala_oi

fala_oi()'''


# Exemplo de package: importação de não somente um módulo, mas uma pasta com módulos

import aula99_package

# Execução de uma função dentro de um módulo, dentro de um package

print (aula99_package.fala_oi())






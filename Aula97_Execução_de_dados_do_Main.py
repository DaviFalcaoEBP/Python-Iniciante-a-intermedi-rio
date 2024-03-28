# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

'''try:
    import sys
    sys.path.append("/home")
except ModuleNotFoundError:
    ...

import Módulo_python'''

# O que está acontecendo necesse caso são dois exemplos de importação:

# 1. Importação de todo o módulo
import Aula97_Importação_de_dados_Main

# 2. Importação de uma variável do módulo
from Aula97_Importação_de_dados_Main import variavel_modulo

# Utilização da variável vindo do arquivo main
print (variavel_modulo)


print ("Este módulo se chama", __name__)



import importlib

# Importação de todos os dados do módulo Main criado
import Aula98_Importação_de_dados_Main

# Impressão somente da variável por meio da utilização de .
print(Aula98_Importação_de_dados_Main.variavel)

# Utilização de uma iteração com for para com a função do módulo importLib, reload, recarregar a variável importada
# da aula 98 Main. Isto ocorrendo 10 vezes
for i in range(10):
    # Recarrega o módulo para refletir alterações no código-fonte
    importlib.reload(Aula98_Importação_de_dados_Main)
    print(f'Módulo recarregado - Iteração {i + 1}')

print("Fim")
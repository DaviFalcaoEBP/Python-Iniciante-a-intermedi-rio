# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# Essa é a função decoradores
# Função externa que tem entrada uma outra função

def criar_funcao(func):
    # Função interna que aceita qualquer tipo de argumento nomeado e não nomeaado
    def interna(*args, **kwargs):
        # Ação de pré checagem de decoração
        print ("Vou te decorar")
        # Desempacotamento dos argumentos empacotados em tupla
        for arg in args:
            # Execucao de função externa e string. Principal ação: Checar se é uma string
            e_string(arg)
        # Criação de uma variável resultado que irá voltar para a função criar função
        resultado = func(*args, **kwargs)
        # Ação pós decoração
        print ("Ok, você foi decorado")
        # Retorno da variável resultado 
        return resultado

    # Execução da função interna
    return interna

# Aplicação de @ para que toda vez que for executado a função inverte string tbm ocorra a da criar função
@criar_funcao
def inverte_string(string):
    return string[::-1]

# Função que faz checagem com isistance se o valor passado é uma str, levantando erro se não
def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Deveria ser uma string")

#inverte_string_checando_parametro = criar_funcao(inverte_string)

#invertida = inverte_string_checando_parametro(123)
    
invertida = inverte_string('123')
print(invertida)

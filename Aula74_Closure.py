"""
Closure e funções que retornam outras funções
"""


'''def criar_saudacao (saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

Falar_bom_dia = criar_saudacao ("Bom dia")
Falar_boa_noite = criar_saudacao ("Boa noite")

for nome in ["Maria", "Joana", "Luiz"]:
    print (Falar_bom_dia(nome))
    print (Falar_boa_noite(nome))



print(Falar_bom_dia("Luiz"))
print (Falar_boa_noite("Luiz"))

'''

lista = ["João", "Davi", "Pedro"]


'''
def saudacao():
    mensagens = []
    for nome in lista:
        for saudacao in saudacoes:
            mensagem = f"{saudacao}, {nome}"
            mensagens.append(mensagem)
    return mensagens

# Chamando a função e armazenando as mensagens em uma variável
mensagens = saudacao()

# Imprimindo as mensagens
for mensagem in mensagens:
    print(mensagem)'''


# Função closure, duas funções que se comunicam no sentido que a interna pode acessar dados da externa, mas não o contrário
def saudacoes (saudacao):
    def saudar (nome):
      return (f"{saudacao}, {nome}")
    return saudar


Falar_bom_dia = saudacoes ("Bom dia")

for nome in lista:
   print(Falar_bom_dia ("Davi"))



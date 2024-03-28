
#Try, except, else e finally

try:
    print ("ABRIR ARQUIVO")
    8 / 0

except ZeroDivisionError:
    print ("Dividiu por zero")

else: # Esse tipo  só aparece se a condição não for cumprida no try
    print ("Não deu erro")
finally: # Este tipo aparece não importando se o try de certo ou não, bom sistema de lembrete de código
    print ("FECHAR ARQUIVO")

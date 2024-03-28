# Exemplo de uso dos sets


# Jogo de adivinhação

'''letras = set()
cont = 0

while True:
    letra = input ("Adivinhe:")
    letras.add (letra.lower())
    cont += 1

    if "l" in letras:
        print ("Acertou")
        print (f"tentativas {cont}")
        break
    print (letras)
'''















# Sets são úteis no sentido de organizar dados somente uma vez dentro de um conjunto

# Criação de um set vazio para armazenar dados
lista = set()

# Criação de um contador para determinar o número de tentativas
contador = 0

# Criação de um loop while para iterar até que o usuário acerte a letra "l"
while True:
    letra = input("Adivinhe: ")

    # Determinação do valor para acabar e utilizar o break para quebrar o loop do while
    if letra == "l":
        print("PARABÉNS")
        break
    else:
        # Adição de valores errados ao set pela utilização de .add e depois inserção como minúsculo
        lista.add(letra.lower())
        print(lista)

        # Adição de um valor ao contador por número de tentativas
        contador += 1

# Impressão do número de tentativas
print("Número de tentativas:", contador)














'''
letras = set()
while True:
    letra = input("Digite:  ")
    letras.add (letra.lower())

    if "l" in letras:
        print ("PARABÉNS")
        break

    print (letras)'''
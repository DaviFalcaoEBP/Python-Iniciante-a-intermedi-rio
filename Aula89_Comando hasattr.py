

#dir, hasattr e gettattr em phyton

string = "Luiz"

# Comando hasattr serve no sentido de atuar na checagem se um objeto pode ser iterado por uma determinada método ou não
# Sendo assim um boolean

if hasattr (string, "upper"):
    print ("Existe upper")
    print (string.upper())


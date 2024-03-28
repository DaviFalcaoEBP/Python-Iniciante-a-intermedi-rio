

# count é um iterador sem fim


from itertools import count


#count não tem fim, ele gera número infinitos
c1 = count ()
r1 = range (10)

print ("c1", hasattr(c1, "__iter__"))
print ("c1", hasattr(c1, "__next__"))

print ("count")


for i in c1:
    if i > 100:
        break
    print (i)
print ("range")

for i in r1:
    if i > 100:
        break
    print (i)
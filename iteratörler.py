sehir=["Adana","Ankara","izmir","mersin"]

iteratör=iter(sehir)
print(next(iteratör))
print(next(iteratör))
print(next(iteratör))
print(next(iteratör))
print("\n")                #aslında ikisi aynı şey for içinde iteratorler var

for i in sehir:
    print(i)
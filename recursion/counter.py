def counter(lista):
    if lista == []:
        return 0
    return 1 + counter(lista[1:])

print(counter([1,2,3,4,5]))
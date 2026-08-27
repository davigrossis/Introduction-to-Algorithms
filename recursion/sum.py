def sum(lista):
    if lista == []:
        return 0
    return lista[0] + sum(lista[1:])

print(sum([2,4,6]))
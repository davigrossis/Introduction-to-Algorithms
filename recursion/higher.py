def higher(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    maxHigh = higher(lista[1:])
    return lista[0] if lista[0] > maxHigh else maxHigh
        
        
print(higher([1,2,3,4,5,6,7]))
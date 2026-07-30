A = [int(x) for x in input("Digite os elementos de A separados por espaço: ").split()]
v = int(input("Digite o valor v: "))

resultado = None

for i in range(len(A)):
    if A[i] == v:
        resultado = i
        break

if resultado != None:
    print("Indice", resultado)
    print(A[resultado])
    print(A)
else:
    print(None)
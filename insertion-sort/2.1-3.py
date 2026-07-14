# Considere o problema de busca:
# Entrada: Uma sequência de n números A = 〈a1, a2, ..., an〉e um valor v.
# Saída: Um índice i tal que v = A[i] ou o valor especial NIL, se v não aparecer em A.

# Escreva o pseudocódigo para busca linear, que faça a varredura da sequência, procurando por v. Usando
# um invariante de laço, prove que seu algoritmo é correto. Certifique-se de que seu invariante de laço satisfaz
# as três propriedades necessárias.

A = [int(x) for x in input("Digite os elementos de A separados por espaço: ").split()]
v = int(input("Digite o valor v: "))

for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key
    resultado = i if A[i] == v else None

if resultado != None:
    print ("Indice ", resultado)
    print (A[resultado])
    print (A)
else: 
    print(None)
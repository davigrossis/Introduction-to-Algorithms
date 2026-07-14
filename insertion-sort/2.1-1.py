# Usando a Figura 2.2 como modelo, ilustre a operação de Insertion-Sort no arranjo A = 〈31, 41, 59, 26, 41, 58〉.

A = [31, 41, 59, 26, 41, 58]

for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key

print("Arranjo final: A=", A)
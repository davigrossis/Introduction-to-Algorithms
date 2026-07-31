#Considere o problema de somar dois inteiros binários de n bits, armazenados em dois arranjos de n elementos
#A e B. A soma dos dois inteiros deve ser armazenada em forma binária em um arranjo de (n + 1) elementos
#C. Enuncie o problema formalmente e escreva o pseudocódigo para somar os dois inteiros.

import random

def soma(A, B):
    n = len(A)
    C = [0] * (n + 1)

    carry = 0

    for i in range(n - 1, -1, -1):
        s = A[i] + B[i] + carry

        C[i + 1] = s % 2
        carry = s // 2

    C[0] = carry

    return C

n = int(input("Digite o número de bits (n): "))

A = [random.randint(0, 1) for _ in range(n)]
B = [random.randint(0, 1) for _ in range(n)]

print("A =", A)
print("B =", B)
C = soma(A, B)
print(C)




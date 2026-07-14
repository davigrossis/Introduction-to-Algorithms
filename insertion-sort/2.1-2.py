# Reescreva o procedimento Insertion-Sort para ordenar em ordem não crescente, em vez da ordem não decrescente.

A = [31,41,59,26,41,58]

for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i>=0 and A[i]<key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key
print("Arranjo: ", A)
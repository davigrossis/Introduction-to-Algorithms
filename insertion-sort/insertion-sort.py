A = [5,2,4,6,1,3]

for j in range(1, len(A)):
    key = A[j] 
    print("valor da chave: ", key)
    i = j - 1
    print("valor de i: ", i)
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        print("valor de i pós while: ", i)
        i -= 1
    A[i + 1] = key
    print("valor de A[i+1]", A[i + 1])
    print("string final da ",j," interação:", A)
print(A)
    

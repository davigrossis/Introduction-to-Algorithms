def max_media(nums, k):
    soma =  sum(nums[:k])
    melhor = soma

    for right in range(k, len(nums)):
        soma += nums[right]
        soma -= nums[right - k]
        melhor = max(melhor, soma)

    return  melhor / k

print(max_media([1, 12, -5, -6, 50, 3], 4))

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

def searchInsert(nums, target):
    alto = len(nums) - 1
    baixo = 0
    print("tamanho:", len(nums))
    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = nums[meio]
        if chute == target:
            return meio
        if chute > target:
            alto = meio - 1
            print("Meio a:", meio)
        else: 
            baixo = meio + 1
            print("Meio b:", meio)

    return baixo
    

nums1 = [1,3,5,6] 
nums2 = [1,3,5,6]
nums3 = [1,3,5,6]
nums4 = [1,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]

print(searchInsert(nums1, 5))
print(searchInsert(nums2, 2))
print(searchInsert(nums3, 7))
print(searchInsert(nums4, 12))
    

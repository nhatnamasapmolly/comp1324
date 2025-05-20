from typing import List
def maxSubArray(nums: List[int]) -> List:
    n = len(nums)
    M = [0] * n
    M[0] = nums[0]
    for i in range(1, n):
        M[i] = max(M[i - 1] + nums[i], nums[i])
    
    maxVar = 0

    for i in range(1,n):
        if M[i] > max:
            max = M[i]
            idx = i
    
    return nums[idx, max + 1]


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

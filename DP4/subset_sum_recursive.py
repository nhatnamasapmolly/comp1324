def subset_sum(nums, target): 
    def subset_sum_helper(nums, target, n):
        if target == 0:
            return True
        if n == 0:
            return False
        
        return subset_sum_helper(nums, target, n - 1) or subset_sum_helper(nums, target - nums[n - 1], n - 1)
        
    return subset_sum_helper(nums, target, len(nums))



print(subset_sum([3,5,4,8], 11))
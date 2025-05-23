import numpy as np
def subset_sum_bottom_up(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # Initialize the first column to True

    for i in range(n + 1):
        dp[i][0] = True

    for j in range(1, target + 1):
        dp[0][j] = False

    for i in range(1, n+1):
        for j in range(1, target + 1):
            if j >= nums[i-1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i-1]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(np.array(dp))
    return dp[n][target]


def subset_sum_bottom_up_retrieve_array(nums, target):
    def subset_sum_bottom_up_helper(nums, target):
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # Initialize the first column to True

        for i in range(n + 1):
            dp[i][0] = True

        for j in range(1, target + 1):
            dp[0][j] = False

        for i in range(1, n+1):
            for j in range(1, target + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(np.array(dp))
        return dp
    dp = subset_sum_bottom_up_helper(nums, target)
    n = len(nums) 
    subset = []
    val = target
    while val > 0 and n > 0:
        if dp[n][val-nums[n-1]] and val - nums[n-1] >= 0:
            subset.insert(0, nums[n-1])
            val -= nums[n-1]
        n -= 1
    return subset

print(subset_sum_bottom_up([5,4,3,6], 9))

print(subset_sum_bottom_up_retrieve_array([2,8,3,13,7], 13))
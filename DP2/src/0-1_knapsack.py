import numpy as np


def knapsack(value, weight, capacity):
    def dp(value, weight, capacity):
        n = len(value)
        dp = [(capacity+1)*[0] for i in range(n)]  
        for i in range(1, n):
            for j in range(1, capacity+1):
                if j >= weight[i]:
                    dp[i][j] = max(dp[i-1][j], value[i] + dp[i-1][j-weight[i]])
                else: 
                    dp[i][j] = dp[i-1][j]
            
        return dp
    
    dp_arr = dp(value, weight, capacity)
    n=len(dp_arr)
    i=n-1
    j= capacity
    sol=[]
    while i>0 and j>0:
        if dp_arr[i][j]!=dp_arr[i-1][j]:  
            sol.insert(0,i)
            j-=weight[i]
        i-=1
    return sol
    

value = [0,2,4,5,6]
weight= [0,3,6,7,8]
capacity = 13

print(knapsack(value,weight,capacity))

#O(n x capacity) time
#O(n x capacity) space
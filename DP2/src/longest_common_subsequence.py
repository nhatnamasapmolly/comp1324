import numpy as np
def longest_common_subsequence(string1, string2):
    def lcs_dp(string1, string2): 
        n = len(string1)
        m = len(string2)
        dp = [[0 for _ in range(m+1)] for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1,m+1):
                print(i,j)
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            

        return dp
    
    L = []
    i = len(string1)
    j = len(string2)
    M = lcs_dp(string1, string2)
    print(np.array(M))
    while i > 0 and j > 0:
        if string1[i-1] == string2[j-1]:
            L = [string1[i-1]] + L[:]
            i,j = i-1,j-1
        else: 
            if M[i-1][j] > M[i][j-1]:
                i = i -1 
            else:
                j = j-1
    return L



string1 = "abc"
string2 = "def"
print(longest_common_subsequence(string1, string2))
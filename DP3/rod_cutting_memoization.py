

def rod_cutting(length_price, length):
    memo = [0] * (length + 1)
    for i in range(1, length + 1):
            memo[i] = float('-inf')
    def dp(length_price, length):
        if memo[length] > 0:
            return memo[length]

        if length == 0:
            return 0
        
        m = float('-inf')
        for i in range(1, length + 1):
            m = max(m, length_price[i] + rod_cutting(length_price, length - i))
        
        memo[length] = m
        return memo[length]
    print(memo)
    return dp(length_price, length)


length_price = [0, 1, 5, 8, 9]
length = 4
print(rod_cutting(length_price, length))


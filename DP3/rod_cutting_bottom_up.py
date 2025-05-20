def rod_cutting_bottom_up(length_price, length):
    memo = [float('-inf')] * (length + 1)
    memo[0] = 0
    for i in range(1, length + 1):
        m = float('-inf')
        for j in range(1, i+1):
            print(memo)
            print(j)
            m = max(m, length_price[j] + memo[i - j])
        memo[i] = m

    print(memo)
    return memo[length]



length_price = [0, 1, 5, 8, 9]
length = 4
print(rod_cutting_bottom_up(length_price, length))

   
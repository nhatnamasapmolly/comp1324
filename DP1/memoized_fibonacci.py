def memoized_fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoized_fibonacci(n - 1, memo) + memoized_fibonacci(n - 2, memo)
    return memo[n]



print(memoized_fibonacci(10))
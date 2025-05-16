def bottom_up_fibonacci(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    if n <= 1:
        return n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


print(bottom_up_fibonacci(10))
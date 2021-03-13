def fibonacci(n):
    if n <= 1:
        return n

    return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibonacci_memoization(n, table):
    if n not in table:
        table[n] = fibonacci_memoization(n - 1, table) + fibonacci_memoization(n - 2, table)
    return table[n]

table = {0: 0, 1: 1}
print(fibonacci_memoization(5, table))
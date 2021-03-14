# FibonacciDP.py 
# Programa para mostrar un indice de la serie de Fibonacci, esto
# se logra usando la recursividad tipo Head y despues con
# recursion tipo Tail para evitar un stack overflow.
# Tambien se calcula usando Dynamic Programming, y asi lograr que
# sea de O(n).
# Miguel Angel Sanchez Mares mares112358@gmail.com

# Fibonacci Head Recursion.
def fibonacci_head(n):
    if n <= 1:
        return n

    return fibonacci_head(n - 1) + fibonacci_head(n - 2)

# Fibonacci Tail Recursion.
def fibonacci_tail(n, acumulador1 = 1, acumulador2 = 0):
    if n == 1:
        return acumulador1
    suma = acumulador1 + acumulador2
    return fibonacci_tail(n - 1, suma, acumulador1)

# Fibonacci memoization (enfoque Top-Down) O(N)
def fibonacci_memoization(n, table):
    if n not in table:
        table[n] = fibonacci_memoization(n - 1, table) + fibonacci_memoization(n - 2, table)
    return table[n]

# Fibonacci tabulation (enfoque Bottom-Up) O(N)
def fibonacci_tabulation(n, table):
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

table = {0: 0, 1: 1}

print(fibonacci_head(35))
print(fibonacci_tail(35))
print(fibonacci_memoization(35, table))
print(fibonacci_tabulation(35, table))
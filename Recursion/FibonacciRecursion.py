# Fibonacci_Recursion 
# Programa para mostrar un indice de la serie de Fibonacci, esto
# se logra usando la recursividad tipo Head y despues con
# recursion tipo Tail para evitar un stack overflow.
# Miguel Angel Sanchez Mares mares112358@gmail.com

# Head Recursion
def fibonacci_head(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    # Llamada recursiva
    fib1 = fibonacci_head(number - 1)
    fib2 = fibonacci_head(number - 2)

    # Operaciones
    resultado = fib1 + fib2
    return resultado

# Tail Recursion
def fibonacci_tail(number, acumulador1 = 1, acumulador2 = 0):
    if number == 1:
        return acumulador1
    suma = acumulador1 + acumulador2
    return fibonacci_tail(number - 1, suma, acumulador1)


print('Salida usando Head recursion:', fibonacci_head(17))
print('Salida usando Tail recursion:', fibonacci_tail(17))
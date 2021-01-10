# Factorial_Recursion 
# Programa para calcular el factorial de un numero, se muestra
# como calcularlo usando la recursividad tipo Head y despues 
# se transforma en una recursion tipo Tail para evitar un stack
# overflow (para fact_tail, usar result = 1 en la llamada de la funcion).
# Miguel Angel Sanchez Mares mares112358@gmail.com

def fact_head(number):
    if number == 1:
        return 1
    return number * fact_head(number - 1)

def fact_tail(number, result):
    if number == 1:
        return result
    return fact_tail(number - 1, result * number)

print(fact_head(8))
print(fact_tail(8, 1))
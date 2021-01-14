# Busqueda_lineal_recursiva
# Algoritmo para hacer la busqueda de un elemento
# dentro de un arreglo de manera recursiva.
# Si el elemento no esta dentro del arreglo, se regresara un -1
# El orden del algoritmo es de O(N)
# USAR BUSQUEDA LINEAL SI EL ARREGLO NO ESTA ORDENADO
# mares112358@gmail.com

def linear_search_recursive(array, element, n = 0):
    if n >= len(array):
        return -1
    if array[n] == element:
        return n

    return linear_search_recursive(array, element, n + 1)

array = [4, 34, 2, 10, 150, 56]

print(linear_search_recursive(array, 2))
# Busqueda_binaria
# Algoritmo para hacer la busqueda de un elemento
# dentro de un arreglo mediante busqueda binaria.
# Si el elemento no esta dentro del arreglo, se regresara un -1.
# Complejidad del tiempo de ejecución O(logN).
# PARA LA BUSQUEDA BINARIA EL ARREGLO DEBE ESTAR ORDENADO.
# mares112358@gmail.com

def binary_search(array, element):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = int((right + left) / 2)
        if array[middle] == element:
            return middle
        elif array[middle] > element:
            right = middle - 1
        else:
            left = middle + 1
    return -1

array = [3, 6, 8, 9, 13, 26]

print(binary_search(array, 8))
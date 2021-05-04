# Busqueda_binaria_recursiva
# Algoritmo para hacer la busqueda de un elemento
# dentro de un arreglo mediante busqueda binaria de manera recursiva.
# Si el elemento no esta dentro del arreglo, se regresara un -1.
# Complejidad del tiempo de ejecución O(logN).
# PARA LA BUSQUEDA BINARIA EL ARREGLO DEBE ESTAR ORDENADO.
# mares112358@gmail.com

def binary_search_recursive(array, elemento, left, right):
    # Si left es mayor a right, los indices se han cruzado 
    # y el elemento buscado no esta en el arreglo.
    if left > right:
        return -1

    # Genera el indice que esta a la mitad del arreglo.
    middle = (right + left) // 2

    # Se encontro el elemento.
    if array[middle] == elemento:
        return middle

    # El elemento se encuentra a la izquierda del arreglo
    elif array[middle] > elemento:
        return binary_search_recursive(array, elemento, left, middle-1)
    
    # El elemento se encuentra a la derecha del arreglo.
    elif array[middle] < elemento:
        return binary_search_recursive(array, elemento, middle+1, right)

array = [3, 6, 8, 9, 13, 26]
print(binary_search_recursive(array, 13, 0, len(array) - 1))
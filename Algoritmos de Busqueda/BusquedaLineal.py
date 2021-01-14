# Busqueda_lineal
# Algoritmo para hacer la busqueda de un elemento
# dentro de un arreglo. Si el elemento no esta dentro
# del arreglo, se regresara un -1
# El orden del algoritmo es de O(N)
# USAR BUSQUEDA LINEAL SI EL ARREGLO NO ESTA ORDENADO
# mares112358@gmail.com


def linear_search(array, element):
    for index in range(len(array)):
        if array[index] == element:
            # si se encuentra el elemento se regresa el indice
            return index
    # si el elemento no se encuentra se regresa un -1
    return -1

array = [4, 34, 2, 10, 150, 56]

print(linear_search(array, 150))
def median_algorithm(array, k):
    #Divide array en sub-listas de longitud 5
    chunks = [array[i:i+5] for i in range(0, len(array), 5)]
    median_line = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    
    #El pivote es la media de las medias
    pivot_value = sorted(median_line)[len(median_line)//2]

    #Fase de particion
    left_array = [n for n in array if n < pivot_value]
    right_array = [n for n in array if n > pivot_value]

    pivot_index = len(left_array)

    #Fase de seleccion
    if k > pivot_index:
        return median_algorithm(right_array, k - len(left_array) - 1)
    elif k < pivot_index:
        return median_algorithm(left_array, k)
    else:
        return pivot_value

array = [3, 7, 8, 10, 15, 20, 1, -1, 18, 4, 9, 12, 0, 16, 14, 17, 29]
print(median_algorithm(array, 0))
print(median_algorithm(array, 1))
print(median_algorithm(array, 2))
print(median_algorithm(array, 3))
print(median_algorithm(array, 4))
print(median_algorithm(array, 5))
print(median_algorithm(array, 6))
print(median_algorithm(array, 7))
print(median_algorithm(array, 8))
def quick_sort(Elementos, izquierda, derecha):
    pivote = derecha-1
    derecha = derecha - 2
    
    while izquierda <= derecha:
        if izquierda == derecha:
            break
        if Elementos[izquierda] < Elementos[pivote]:
            izquierda += 1
        elif Elementos[derecha] > Elementos[pivote]:
            derecha -= 1
        else:
            auxiliar = Elementos[izquierda]
            Elementos[izquierda] = Elementos[derecha]
            Elementos[derecha] = auxiliar
            izquierda += 1
            derecha -= 1
    
    pivote = derecha
    auxiliar = Elementos[izquierda]
    Elementos[izquierda] = Elementos[pivote]
    Elementos[pivote] = auxiliar

    quick_sort(Elementos, 0, pivote)

Elementos = []
primer_elemento = 0
n_elementos = int(input('Numero de elementos: '))

for indice in range(n_elementos):
    Elementos.append(int(input('Elemento {}: '.format(indice))))

print(Elementos)
quick_sort(Elementos, primer_elemento, n_elementos)
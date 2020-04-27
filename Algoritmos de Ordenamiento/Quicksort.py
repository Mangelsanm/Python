def quick_sort(Elementos, inicio, fin):
    if inicio < fin:
        global izquierda
        pivote = fin-1
        izquierda = inicio
        derecha = fin - 2
        
        while izquierda <= derecha:
            while Elementos[izquierda] < Elementos[pivote]:
                izquierda += 1
            while Elementos[derecha] > Elementos[pivote]:
                derecha -= 1
            if izquierda < derecha:
                auxiliar = Elementos[izquierda]
                Elementos[izquierda] = Elementos[derecha]
                Elementos[derecha] = auxiliar

        auxiliar = Elementos[izquierda]
        Elementos[izquierda] = Elementos[pivote]
        Elementos[pivote] = auxiliar

        pivote = izquierda
        quick_sort(Elementos, inicio, pivote)
        quick_sort(Elementos, pivote+1, fin)

Elementos = []
primer_elemento = 0
n_elementos = int(input('Numero de elementos: '))

for indice in range(n_elementos):
    Elementos.append(int(input('Elemento {}: '.format(indice))))

print(Elementos)
quick_sort(Elementos, primer_elemento, n_elementos)
print(Elementos)
def quick_sort(Elementos, izquierda, derecha):
    pivote = derecha-1
    derecha = derecha - 2
    
    if izquierda < derecha:
    
        while izquierda <= derecha:
            if izquierda == derecha:
                break
            while Elementos[izquierda] < Elementos[pivote]:
                izquierda += 1
            while Elementos[derecha] > Elementos[pivote] and izquierda < derecha:
                derecha -= 1
            if izquierda < derecha:
                auxiliar = Elementos[izquierda]
                Elementos[izquierda] = Elementos[derecha]
                Elementos[derecha] = auxiliar    
        
        auxiliar = Elementos[izquierda]
        Elementos[izquierda] = Elementos[pivote]
        Elementos[pivote] = auxiliar

        pivote = izquierda
        quick_sort(Elementos, 0, pivote)
        quick_sort(Elementos, pivote+1, 10)

Elementos = []
primer_elemento = 0
n_elementos = int(input('Numero de elementos: '))

for indice in range(n_elementos):
    Elementos.append(int(input('Elemento {}: '.format(indice))))

print(Elementos)
quick_sort(Elementos, primer_elemento, n_elementos)
print(Elementos)
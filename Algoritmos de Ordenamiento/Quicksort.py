def quick_sort(Elementos, izquierda, derecha):
    if izquierda < derecha:
        global i
        pivote = derecha-1
        i = izquierda
        j = derecha - 2
        
        while i <= j:
            #if i == j:
            #    break
            while Elementos[i] < Elementos[pivote]:
                i += 1
            while Elementos[j] > Elementos[pivote]:# and i < j:
                j -= 1
            if i < j:
                auxiliar = Elementos[i]
                Elementos[i] = Elementos[j]
                Elementos[j] = auxiliar

        #if Elementos[i] > Elementos[pivote]:
        auxiliar = Elementos[i]
        Elementos[i] = Elementos[pivote]
        Elementos[pivote] = auxiliar

        pivote = i
        quick_sort(Elementos, izquierda, pivote)
        quick_sort(Elementos, pivote+1, derecha)

Elementos = []
primer_elemento = 0
n_elementos = int(input('Numero de elementos: '))

for indice in range(n_elementos):
    Elementos.append(int(input('Elemento {}: '.format(indice))))

print(Elementos)
quick_sort(Elementos, primer_elemento, n_elementos)
print(Elementos)
def brb_bidi(elementos):
    n_elementos = len(elementos) - 1
    
    indice_izquierdo = 0
    indice_derecho = n_elementos

    while indice_izquierdo < indice_derecho:
        for i in range(indice_izquierdo, indice_derecho):
            if elementos[i] > elementos[i+1]:
                auxiliar = elementos[i]
                elementos[i] = elementos[i+1]
                elementos[i+1] = auxiliar
        
        for j in range(indice_derecho, indice_izquierdo, -1):
            if elementos[j] < elementos[j-1]:
                auxiliar = elementos[j]
                elementos[j] = elementos[j-1]
                elementos[j-1] = auxiliar
        
        indice_izquierdo += 1
        indice_derecho -= 1

elementos = []
n_elementos = int(input('Numero de elementos: '))

for i in range(n_elementos):
    elementos.append(int(input('Valor del indice {}: '.format(i))))

print(elementos)
brb_bidi(elementos)
print(elementos)
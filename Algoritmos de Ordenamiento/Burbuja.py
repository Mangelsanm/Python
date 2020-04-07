def burbuja(Elementos):

    n_elementos = len(Elementos) - 1
    rango = range(len(Elementos))

    for i in rango:
        for j in range(n_elementos - i):
            if Elementos[j] > Elementos[j+1]:
                auxiliar = Elementos[j]
                Elementos[j] = Elementos[j+1]
                Elementos[j+1] = auxiliar

Elementos = []
n_elementos = int(input('Numero de elementos: '))

for i in range(n_elementos):
    Elementos.append(int(input('Valor del indice {}: '.format(i))) )

print(Elementos)
burbuja(Elementos)
print(Elementos)
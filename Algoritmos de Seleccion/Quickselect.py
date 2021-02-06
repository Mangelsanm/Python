import random

class QuickSelect:
    """Algoritmo QuickSelect"""

    # Constructor
    def __init__(self, array):
        self.array = array
        self.left_index = 0
        self.right_index = len(array) - 1

    def run(self, k):
        return self.select(self.left_index, self.right_index, k-1)

    # ESTA ES LA FASE DE PARTICION
    def partition(self, left_index, right_index):
        # Genera un numero entero aleatorio entre 0 y len de array
        pivot_index = random.randint(left_index, right_index)
        self.swap(pivot_index, right_index)

        for i in range(left_index, right_index):
            if self.array[i] < self.array[right_index]:
                self.swap(i, left_index)
                left_index += 1
        
        self.swap(left_index, right_index)

        return left_index

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    # ESTA ES LA FASE DE SELECCION
    def select(self, left_index, right_index, k):
        pivot_index = self.partition(left_index, right_index)

        # Fase de seleccion, cuando comparamos el pivote con k
        if pivot_index < k:
            # Se descarta el sub-arreglo de la izquierda y se trabaja
            # con el arreglo de la derecha.
            return self.select(pivot_index, right_index, k)
        elif pivot_index > k:
            # Se descarta el sub-arreglo de la derecha y se trbaja
            # con el arreglo de la inzquierda.
            return self.select(left_index, pivot_index - 1, k)
        
        return self.array[pivot_index]

x = [1, -2, 5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
print(select.run(1))
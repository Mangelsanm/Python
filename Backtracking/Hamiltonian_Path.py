class Hamiltonian_path:

    def __init__(self, Hamiltonian_Matrix):
        self.Hamiltonian_Matrix = Hamiltonian_Matrix
        self.n = len(Hamiltonian_Matrix)
        self.path = [0] #Agregamos a nuestro arreglo el vertice A por default.

    def solve_path(self):
        #Comenzamos con el segundo vertice, ya que el primero lo agregamos por default.
        if self.solve(1):
            self.show_path()
        else:
            print('There is not solution')
    
    def solve(self, position):
        #Si position es igual a n, ya se encontro solucion para n-1
        if position == self.n:
            return True

        for vertex in range(1, self.n):
            if self.is_valid(position, vertex):
                self.path.append(vertex)

                if self.solve(position + 1):
                    return True

                #Backtracking
                self.path.pop()

        return False
    
    def is_valid(self, position, vertex):
        #Para saber si hay conexion entre los vertices, si la posicion de la matriz
        #es igual a cero, no hay conexion entre los vertices.
        if self.Hamiltonian_Matrix[self.path[position - 1]][vertex] == 0:
            return False

        #Verificar si el vertice actual no se ha agregado al path, esto es, para no visitar
        #el mismo path dos veces.
        for i in range(position):
            if self.path[i] == vertex:
                return False

        return True

    def show_path(self):
        for v in self.path:
            print(chr(v + 65), end = ' ') #Cast a char y suma 65 (ASCII) para mostrar los vertices como letras.

# m = [[0, 1, 0, 1, 0, 1],
#      [1, 0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 1, 0],
#      [1, 1, 1, 0, 0, 0],
#      [0, 0, 1, 0, 0, 1],
#      [1, 0, 0, 0, 1, 0]]

m = [[0, 0, 1, 1],
     [0, 0, 1, 1],
     [1, 1, 0, 0],
     [1, 1, 0, 0]]

# m = [[0, 1, 0, 0, 0, 1],
#      [1, 0, 1, 0, 0, 0],
#      [0, 1, 0, 1, 1, 0],
#      [0, 0, 1, 0, 1, 0],
#      [0, 0, 1, 1, 0, 1],
#      [1, 0, 0, 0, 1, 0]]

path = Hamiltonian_path(m)
path.solve_path()
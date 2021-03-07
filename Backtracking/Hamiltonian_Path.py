class Hamiltonian_Path:

    def __init__(self, Hamiltonian_Matrix):
        self.Hamiltonian_Matrix = Hamiltonian_Matrix
        self.n = len(Hamiltonian_Matrix)
        self.path = [0]

    def Hamiltonian_Solve(self):
        if self.solve(1):
            self.show_path()
        else:
            print('There is not solution')
    
    def solve(self, position):
        if position == self.n:
            return True

        for vertex in range(1, self.n):
            if self.is_valid(vertex, position):
                self.path.append(vertex)

                if self.solve(position + 1):
                    return True

                self.path.pop()

        return False
    
    def is_valid(self, vertex, position):
        if self.Hamiltonian_Matrix[self.path[position - 1]][vertex] == 0:
            return False

        for i in range(position):
            if self.path[i] == vertex:
                return False

        return True

    def show_path(self):
        for v in self.path:
            print(v)

m = [[0, 1, 0, 1, 0, 1],
     [1, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 1, 0]]

hamitonian = Hamiltonian_Path(m)
hamitonian.Hamiltonian_Solve()
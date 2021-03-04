
class Queens:

    # Constructor
    def __init__(self, nQueens):
        self.nQueens = nQueens
        self.chess_table = [[0 for i in range(nQueens)] for j in range(nQueens)]
    
    def solve_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print('No hay solucion para este numero de reynas')
    
    def solve(self, col_index):
        # Caso base, col_index llego al limite de la matriz, quiere decir que resolvio el problema.
        if col_index == self.nQueens:
            return True
        
        # Recorremos de manera vertical, para colocar nuestra reyna.
        for row_index in range(self.nQueens):
            if self.valid_position(row_index, col_index):
                self.chess_table[row_index][col_index] = 1

                # Tratamos de buscar la ubicacion de la siguiente reyna.
                if self.solve(col_index + 1):
                    return True

                # Backtrack
                self.chess_table[row_index][col_index] = 0
        # Cuando hemos considerado todos los renglones de una columna
        # y no hemos encontrado una celda valida.
        return False

    def valid_position(self, row_index, col_index):
        # Revisamos horizontalmente si la casilla es valida.
        for i in range(self.nQueens):
            if self.chess_table[row_index][i] == 1:
                return False

        # Revisamos la diagonal superior del lado izquierdo.
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        
        # Revisamos la diagonal inferior del lado izquierdo.
        j = col_index
        for i in range(row_index, self.nQueens):
            if j < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        
        return True

    def print_queens(self):
        for i in range(self.nQueens):
            for j in range(self.nQueens):
                if self.chess_table[i][j] == 1:
                    print(' Q ', end = '')
                else:
                    print(' - ', end = '')
            print('\n')        

if __name__ == '__main__':
    x = Queens(8)
    x.solve_queens()
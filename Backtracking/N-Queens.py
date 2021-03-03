class Queens:

    # Constructor
    def __init__(self, nQueens):
        self.nQueens = nQueens
        self.chess_table = [[0 for i in range(nQueens)] for j in range(nQueens)]
    
    def solve(self, col_index):
        # Caso base, col_index llego al limite de la matriz, quiere decir que resolvio el problema.
        if col_index == self.nQueens:
            return True
        
        # Recorremos de manera vertical, para colocar nuestra reyna.
        for row_index in self.nQueens:
            if self.valid_position(row_index, col_index):
                self.chess_table[row_index][col_index] = 1


x = Queens(4)
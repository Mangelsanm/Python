class KnightsTour:
    def __init__(self, board_size):
        self.board_size = board_size
        # Movimientos del caballo en el tablero de ajedrez, en X y Y.
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

        self.chess_board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def solve_tour(self):
        self.chess_board[0][0] = 0
        if self.solve(1, 0, 0):
            self.show_chess()
        else:
            print('There is not solution for the problem')

    def solve(self, knight, x, y):
        if knight == self.board_size * self.board_size:
            return True
        for move_index in range(len(self.x_moves)):
            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_location(next_x, next_y):
                self.chess_board[next_x][next_y] = knight

                if self.solve(knight + 1, next_x, next_y):
                    return True
                
                self.chess_board[next_x][next_y] = -1
        return False

    def is_valid_location(self, next_x, next_y):
        if next_x < 0 or next_x >= self.board_size:
            return False
        if next_y < 0 or next_y >= self.board_size:
            return False
        if self.chess_board[next_x][next_y] > -1:
            return False

        return True

    def show_chess(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.chess_board[i][j], end = ' ')
            print('\n')

if __name__ == '__main__':
    tour = KnightsTour(5)
    tour.solve_tour()
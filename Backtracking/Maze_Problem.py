class MazeProblem():
    def __init__(self, maze):
        self.maze = maze
        self.size = len(maze)
        # self.solution_table = [[0] * self.size for _ in range(self.size)]
        self.solution_table = [[0 for _ in range(self.size)]  for _ in range(self.size)]
    
    def solve_maze(self):
        if self.solve(0, 0):
            self.show_solution()
        else:
            print('There is not solution')
    
    def solve(self, x, y):
        if self.is_finished(x, y):
            return True

        if self.is_valid(x, y):
            self.solution_table[x][y] = 1

            if self.solve(x + 1, y):
                return True
            if self.solve(x, y + 1):
                return True
            self.solution_table[x][y] = 0
        return False

    def is_finished(self, x, y):
        if x == self.size - 1 and y == self.size - 1:
            self.solution_table[x][y] = 1
            return True
        return False
    
    def is_valid(self, x, y):
        if x < 0 or x >= self.size:
            return False
        if y < 0 or y >= self.size:
            return False
        if self.maze[x][y] == 1:
            return False
        return True        

    def show_solution(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.solution_table[i][j] == 1:
                    print('S', end = ' ')
                else:
                    print('-', end = ' ')
            print('\n')

if __name__ == '__main__':
    m = [[0, 0, 1, 1],
         [0, 0, 0, 1],
         [1, 1, 0, 0],
         [1, 1, 0, 0]]

    maze = MazeProblem(m)
    maze.solve_maze()
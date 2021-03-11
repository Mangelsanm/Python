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

    def is_finished(self, x, y):
        if x == self.size - 1 and y == self.size - 1:
            self.solution_table[x][y] = 1
            return True
        return False

if __name__ == '__main__':
    m = [[0, 0, 1, 1],
         [0, 0, 0, 1],
         [1, 1, 0, 0],
         [1, 1, 0, 0]]

    maze = MazeProblem(m)
    print(maze.solution_table)
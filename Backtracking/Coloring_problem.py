class ColoringProblem:
    def __init__(self, matrix, nColors):
        self.n = len(matrix)
        self.matrix = matrix
        self.nColors = nColors
        self.colors = [0 for i in range(self.n)]

    def coloring_problem(self):
        if self.solve(0):
            self.print()
        else:
            print("There is not solution for this problem")
    
    def solve(self, node_index):
        # Caso base
        if node_index == self.n:
            return True
        
        for color_index in range(1, self.nColors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True
    
    def is_color_valid(self, node_index, color_index):
        for i in range(self.n):
            if self.matrix[node_index][i] == 1 and self.colors[i] == color_index:
                return False
        return True
    
    def print(self):
        for i in range(self.n):
            print(i, self.colors[i])


m = [[0, 1, 1, 0],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]

colors = ColoringProblem(m, 2)
colors.coloring_problem()
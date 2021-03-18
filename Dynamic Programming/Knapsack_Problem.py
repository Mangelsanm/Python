class Knapsack_problem():
    def __init__(self, Knapsack_capacity, weights, profits, number_items):
        self.Knapsack_capacity = Knapsack_capacity
        self.weights = weights
        self.profits = profits
        self.number_items = number_items
        self.S_array = [[0 for _ in range(self.Knapsack_capacity+1)] for _ in range(self.number_items+1)]

    def solveKnapsack(self):
        for i in range(self.number_items + 1):
            for w in range(self.Knapsack_capacity + 1):
                not_taking_item = self.S_array[i-1][w]
        # s[i][w] = Math.max(s[i-1][w], vi + s[i-1][w-wi])
        

    # def Knapsack_recursion(self):
    #     if self.m == 0 or self.n == 0:
    #         return 0
    #     if self.w[self.n-1] > self.m:
    #         return Knapsack_recursion(self.m, self.w, self.v, self.n-1)
    #     else:
    #         included = self.v[self.n-1] + Knapsack_recursion(self.m - self.w[self.n-1], self.w, self.v, self.n-1)
    #         excluded = Knapsack_recursion(self.m, self.w, self.v, self.n-1)

    #         return max(included, excluded)


w = [4, 2, 3]
v = [10, 4, 7]

recursion = Knapsack_problem(5, w, v, 3)
print(recursion.S_array)
import random

class Sort_Select:

    def __init__(self, array):
        self.array = array
        self.first_index = 0
        self.last_index = len(array) - 1

    def sort(self):
        sorted_array = []

        for i in range(1, len(self.array) + 1):
            sorted_array.append(self.run(i))
        
        return sorted_array

    def run(self, k):
        return self.select(self.first_index, self.last_index, k - 1)

    def select(self, first_index, last_index, k):
        pivot_index = self.partition(first_index, last_index)

        if k < pivot_index:
            #checar estos return
            return self.select(first_index, pivot_index - 1, k)
        elif k > pivot_index:
            return self.select(pivot_index + 1, last_index, k)

        return self.array[pivot_index]
    
    def partition(self, first_index, last_index):
        pivot_index = random.randint(first_index, last_index)
        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if(self.array[i] < self.array[last_index]):
                self.swap(i, first_index)
                first_index += 1
        self.swap(first_index, last_index)

        return first_index 

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

array = [5, 3, 6, 0, 2, 4, 8, 9, 7, 1]
select = Sort_Select(array)
print(select.sort())
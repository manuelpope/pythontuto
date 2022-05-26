class GenClass:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        
        self.n += 1
        return self.n if self.n%2 != 0 else self.n+1

g = GenClass(15)

print([x for x in g])

'''
Ouput :
[1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17]

'''

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(GenClass(10))))

'''
Output:
571
'''
class SimpleClass:
    def __init__(self, x, y):
        self.x= x
        self.y = y

    def sum_num (self):
        return self.x + self.y


s = SimpleClass(1,2)
print(s.sum_num())

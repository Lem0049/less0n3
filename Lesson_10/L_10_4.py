class Vector:
    def __init__(self, *args):
        self.coorps = args
        self.size = len(args)

    def get_size(self):
        return self.size

    def __add__(self, other):
        if self.get_size() == other.get_size():
            result = []
            for i in range(self.get_size()):
                result.append(self.coorps[i] + other.coorps[i])

        return Vector(*result)
    @staticmethod
    def information():
        print('Класс Vector создан для векторов')

    def length(self):
        return self.coorps


vect1 = Vector(1, 2, 7)
vect2 = Vector(2, 3, 7)
Vector.information()
print((vect1 + vect2).length())


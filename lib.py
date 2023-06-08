class Point:
    __x = 0
    __y = 0
    __minCoor = 0
    __maxCoor = 8

    def __init__(self, x, y):
        if self.CoorTest(x) and self.CoorTest(y):
            self.__x = x
            self.__y = y
            print(f'created: {self}')
        else:
            raise Exception('нарушены границы числа')

    @classmethod
    def CoorTest(cls, value):
        return cls.__minCoor <= value <= cls.__maxCoor

    def getCoor(self):
        return (self.__x, self.__y)

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    @staticmethod
    def gip(x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def __del__(self):
        print(f'deleted: {self}')

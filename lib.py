class Point:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        print(f'created: {self}')

    def getCoor(self):
        return (self.__x, self.__y)

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def __del__(self):
        print(f'deleted: {self}')
#какое-то изменение
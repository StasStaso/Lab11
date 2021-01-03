from math import pi, sqrt


class TCircle:
    def __init__(self, r=1.0, x=0.0, y=0.0):
        self.__r = r
        self.__x = x
        self.__y = y

    def get_radius(self):
        '''Повертає радіус'''
        return self.__r

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_radius(self, value):
        if value >= 0:
            self.__r = value

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    def s(self):
        return (self.__r ** 2) * pi

    def belonging(self, x, y):
        return self.__r >= sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2)

    def __add__(self, other):
        return TCircle(self.__r + other.__r, self.__x, self.__y)

    def __sub__(self, other):
        if self.__r - other.__r >= 0:
            return TCircle(self.__r - other.__r, self.__x, self.__y)
        else:
            return Exception("Radius will be <0")

    def __mul__(self, other):
        return TCircle(self.__r * other, self.__x, self.__y)

'''Ввід даних для кола'''
radius = float(input("Radius = "))
x = float(input("Insert x: "))
y = float(input("Insert y: "))

'''Створення об'єкту класу'''
obj = TCircle(radius, x, y)
print("----------"*3)

'''Переірка і вивід даних'''
print("Radius = ",obj.get_radius())
print("X = ",obj.get_x())
print("Y = ",obj.get_y())
print("----------"*3)
obj2 =TCircle(1)
dotx = float(input("Input x for dot: "))
doty = float(input("Input y for dot: "))
print("Are dot in Circle: ",obj.belonging(dotx,doty))





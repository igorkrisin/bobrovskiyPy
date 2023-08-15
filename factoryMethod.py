from math import *
class FactoryPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return FactoryPoint(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return FactoryPoint(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = FactoryPoint(2, 3)
    p3 = FactoryPoint.new_cartesian_point(3,4)
    p2 = FactoryPoint.new_polar_point(1, 2)
    print(p, p2)


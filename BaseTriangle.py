from math import *


class Triangle:


    def __init__(self, vertex1, vertex2, vertex3):
        self.x1 = vertex1[0]
        self.y1 = vertex1[1]
        self.x2 = vertex2[0]
        self.y2 = vertex2[1]
        self.x3 = vertex3[0]
        self.y3 = vertex3[1]
        self.l1 = sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        self.l2 = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        self.l3 = sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)

    def perimeter(self):
        return self.l1 + self.l2 + self.l3

    def square(self):  # следствие из формулы Герона
        return sqrt((self.l1 + self.l2 + self.l3) *
                    (self.l1 + self.l2 - self.l3) *
                    (self.l1 - self.l2 + self.l3) *
                    (-self.l1 + self.l2 + self.l3)) / 4

    def isTriangle(self):
        return not (self.l1 + self.l2 == self.l3 or \
                    self.l2 + self.l3 == self.l1 or \
                    self.l1 + self.l3 == self.l2)

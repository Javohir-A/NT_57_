class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = 0.5*(self.a+self.b+self.c)
        return (s*(s - self.a)*(s - self.b)*(s - self.c))**0.5


class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2


class check:
    def __init__(self, triangle: Triangle, square: Square):
        self.triangle = triangle
        self.square = square

    def __str__(self):
        if self.triangle.area() < self.square.area():
            return "The triangle can be placed inside of the square"
        else:
            return "The square can be placed inside of the triangle!"


triangle1 = Triangle(2, 5, 6)
square1 = Square(2)
check1 = check(triangle1, square1)
print(check1.__str__())

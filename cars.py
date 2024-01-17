from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Cannot instantiate an abstract class directly
# my_shape = Shape()  # This will raise an error
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

my_circle = Circle(radius=5)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())

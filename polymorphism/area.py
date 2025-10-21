import math

class Shape:
    def __init__(self, name):
        self.name=name

    def area(self) -> float:
        return 0.0
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius=radius
        if radius < 0:
            raise ValueError("No negative length")
        
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        if width < 0 or length < 0:
            raise ValueError("No negative length")
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
        if base < 0 or height < 0:
            raise ValueError("No negative length")
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle("circle", 3), Rectangle("Rectangle", 4, 5), Triangle("Triangle", 4, 5)]

for a in shapes:
    print(f"{a.name}, has area of {a.area(): .2f}")


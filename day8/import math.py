import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle_obj = Circle(5)
rectangle_obj = Rectangle(4, 6)

shapes = [circle_obj, rectangle_obj]

print("Calculating areas:")
for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area():.2f}")

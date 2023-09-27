class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def info(self):
        return f"Circle with radius: {self.radius}"
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def draw(self):
        return "o"
    
c1 = Circle(2)

print(c1.info())
print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")
print(c1.draw())




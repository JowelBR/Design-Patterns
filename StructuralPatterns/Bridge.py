import abc

# Abstraction of the Color class using ABC
class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fillColor(self):
        pass
    
# Concrete Implementations of Color
class RedColor(Color):
    def fillColor(self):
        return "my color is Red"

class BlueColor(Color):
    def fillColor(self):
        return "my color is Blue"

class VoidColor(Color):
    def fillColor(self):
        return "I don't have any color"
    

# Abstraction class Shape
class Shape:
    def __init__(self, color: Color = VoidColor()):
        self.color = color

    def draw(self):
        pass

# Concrete Implementations of Shape
class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")
        print(self.color.fillColor())

# Concrete Implementations of Shape
class Square(Shape):
    def draw(self):
        print("Drawing a square.")
        if isinstance(self.color, VoidColor):
            print(self.color.nothingColor())
        else:
            print(self.color.fillColor())

# Client Code
red = RedColor()
blue = BlueColor()

circle = Circle(red)
circle.draw()

square = Square(blue)
square.draw()

# Testing with VoidColor
no_color_shape = Circle()
no_color_shape.draw()

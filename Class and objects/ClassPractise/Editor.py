class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length  # -> return area of rectangle


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


# -> return area of circle

class Editor:
    def __init__(self):
        self.rectangle = None
        self.circle = None

    # -> define rectangle and circle
    def create_rectangle(self, width, length):
        self.rectangle = Rectangle(width, length)

    #-> create object rectangle from class rectangle and assign it into rectangle variable

    def create_circle(self, radius):
        self.circle = Circle(radius)

    #-> create new object from circle and assign it into circle atribute

    def change_rectangle(self, factor):
        if self.rectangle is None:
            return
        width, length = self.rectangle.width + factor, self.rectangle.length + factor
        self.create_rectangle(width, length)

    def change_circle(self, factor):
        if self.circle is None:
            return
        radius = self.circle.radius + factor
        self.create_circle(radius)

    def change(self, factor):
        self.change_rectangle(factor)
        self.change_circle(factor)

    def print(self):
        if self.rectangle is not None:
            print("Rectangle area:", self.rectangle.calculate_area())
        if self.circle is not None:
            print("Circle area:", self.circle.calculate_area())


editor = Editor()
editor.create_rectangle(3, 5)
editor.print()
editor.create_circle(5)
editor.change(2)
editor.print()

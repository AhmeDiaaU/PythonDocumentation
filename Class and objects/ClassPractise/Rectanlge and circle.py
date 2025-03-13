class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area_c(self):
        return 3.14 * self.radius * self.radius


c = circle(5)
print(c.calculate_area_c())
r = rectangle(2,5)
print(r.calculate_area())
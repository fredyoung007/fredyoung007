class Circle:
    def __init__(self, radius=1, color="blue"):
        self.radius = radius
        self.color = color

    def cir(self):
        return self.radius * 2 * 3.14


c = Circle(color="red")
print(c.cir())
print(c.color)
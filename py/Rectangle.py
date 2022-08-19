class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.width) + " x " + str(self.height)

class RectangleBound:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rectangles = []

    def __str__(self):
        if len(self.rectangles) == 0:
            return "No rectangles.\n"
        rstr = "Rectangles:\n"
        for r in self.rectangles:
            rstr += "Rectangle: " + str(r) +"\n"
        return rstr

    def add_rectangle(self, rectangle):
        if (self.width > rectangle.width) and (self.height > rectangle.height):
            self.rectangles.append(rectangle)

bound = RectangleBound(200,200)
print(bound)

bound.add_rectangle(Rectangle(20,40))
bound.add_rectangle(Rectangle(40,60))
bound.add_rectangle(Rectangle(400,300))
print(bound)
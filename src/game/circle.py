from shape import Shape
class Circle(Shape):
    def __init__(self, xPos, yPos, radius):
        Shape.__init__(self, xPos, yPos)
        self.radius = radius



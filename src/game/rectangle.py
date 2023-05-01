from shape import Shape


class Rectangle(Shape):
    def __init__(self, xPos, yPos, height, width):
        Shape.__init__(self, xPos, yPos)
        self.height = height
        self.width = width
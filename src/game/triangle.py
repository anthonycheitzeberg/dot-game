from shape import Shape

class Triangle(Shape):
    def __init__(self, xPos, yPos, height, angle):
        Shape.__init__(self,xPos, yPos)
        self.height = height
        self.angle = angle
from src.game.circle import Circle
from src.game.rectangle import Rectangle
from src.game.triangle import Triangle


class Collision():
    def __init__(self):
        self.isCollision = false


    def calculateCollision(self, shape1, shape2):
        if isinstance(shape1, Circle):
            if isinstance(shape2, Rectangle):
                pass
            if isinstance(shape2, Circle):
                pass
            if isinstance(shape2, Triangle):
                pass
        if isinstance(shape1, Rectangle):
            if isinstance(shape2, Rectangle):
                pass
            if isinstance(shape2, Circle):
                pass
            if isinstance(shape2, Triangle):
                pass
        if isinstance(shape1, Triangle):
            if isinstance(shape2, Rectangle):
                pass
            if isinstance(shape2, Circle):
                pass
            if isinstance(shape2, Triangle):
                pass



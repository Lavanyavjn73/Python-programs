from rectangle import Rectangle

class Parallelepiped(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
    
    def Volume(self):
        return self.length * self.breadth * self.height

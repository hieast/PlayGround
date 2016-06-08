class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, deltax=0, deltay=0):
        """Translate the point in the x direction by deltax 
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    def __iter__(self):
        self.current = 0
        return self
    
    def next(self):
        if self.current == 0:
            self.current += 1
            return self.x
        elif self.current == 1:
            self.current += 1
            return self.y
        else:
            raise StopIteration

            
            
point = Point2D(3, 6)
s = str(point)
print s

point = Point2D(3, 6)
lst = list(point)
x = lst[0]
print x

point = Point2D(3, 6)
tup = tuple(point)
print tup
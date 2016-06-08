class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print c
    
print list(Counter(3, 8))

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, deltax=0, deltay=0):
        """Translate the point in the x direction by deltax 
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay
        
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
    
            
    
print tuple(Point2D(3, 8))
        
        
        
        
        
        
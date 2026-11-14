class Rectangle:
    def __init__(self,w,h):
        self.w = w
        self.h = h



    def get_area(self):
        return self.w * self.h 
    def get_peri(self):
        return (self.w +self.h) * 2



r = Rectangle(3,4)
print(r.get_area())
print(r.get_peri())
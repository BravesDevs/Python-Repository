class Coords:
    def __init__(self,leng,bred):
        self.leng = leng
        self.bred = bred

class Square(Coords):
    def __init__(self,leng):
        super().__init__(leng,leng)
            
    def area(self):
        print(self.leng**2) 

square = Square(10)
square.area()
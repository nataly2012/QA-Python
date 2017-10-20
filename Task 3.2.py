class Room:
    def __init__(self, a=None,b=None):
        self.a = a
        self.b = b

    def square(self,a,b):
        return a*b

    def perimeter(self,a,b):
        return 2*(a+b)

figure = Room()
print(figure.square(10,20))
print(figure.perimeter(10,20))


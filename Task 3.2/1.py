class Dot:
    def __init__(self, a=None,b=None):
        self.a = a
        self.b = b

    def begin(self,a,b):
        x=0
        y=0
        dif1 = a-y
        dif2 = b-x
        return dif1,dif2

    def difference(self, a, b):
        dif1 = a - figure2.a
        dif2 = b - figure2.b
        return dif1, dif2


figure1 = Dot()
print(figure1.begin(-10,20))

figure2 = Dot()
figure2.a = 8
figure2.b = 12

print(figure1.difference(10,20))



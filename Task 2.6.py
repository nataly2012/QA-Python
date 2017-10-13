# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и
# если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).

def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("triangle exists")
    elif a == b != c or a == c != b or b == c != a:
         print ("Isosceles triangle")
    elif a == b == c:
         print ("Equilateral triangle")
    elif a != b != c and b != c:
         print ("Versatile triangle")
    else:
        print ("Not a triangle")

res = triangle(5,0,5)
print (res)

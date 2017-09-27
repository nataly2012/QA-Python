import math
#Task 2.1

a=179
b=971
c = math.sqrt(a**2+b**2)
print(c)

#Task 2.2-3

num = input("Введите число:")
if len(num)==2:
    print ("Ваше число содержит "+ str(num[0])+" дестяков")
elif len(num)==3:
    n=int(num)
    a=n%10
    n=n//10
    b=n%10
    n=n//10
    c=n%10
    print("Cумма цифр числа " + str(a+b+c))
else:
    print ("Ваше число слишком большое")

#Task 2.4

num=input("print number:")
n=int(num)
if n%2==0:
    print(str(n+2))
else:
    print(str(n+1))

#Task 2.5

num = float(input("Print float number:"))
print(num - int(num))

#Task 2.6

num = float(input("Print float number:"))
n=int(num*10)%10
print(n)
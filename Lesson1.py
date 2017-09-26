import math

#Task 1.1
#
# string=input("Print something here:")
# if string.isdigit():
#     print("You " + str(string) + " has numbers")
# else:
#    print("You " + str(string) + " has letters")

#Task 1.4
# text="Homework"
# print(text.center(100, ' '))

#Task 1.5
# text2 = (input("Paste text here:"))
# print(text2.title())

#Task 2.5
# num = float(input("Print float number:"))
# print(num - int(num))

#Task 2.6
# num = float(input("Print float number:"))
# n=int(num*10)%10
# print(n)

#Task3
# year = input("Please type your year of birth here:")
# year = int(year)
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("YES, you birth year is a leap-year")
# else:
#     print("NO, you birth year is not a leap-year")

#Task4
# a=input("a=")
# a=int(a)
# b=input("b=")
# b=int(b)
# c=input("c=")
# c=int(c)
# if a + b > c and a + c > b and b + c > a:
# 	print("Yes, triangle exists ")
# else:
# 	print("No, triangle does not exist")



# text = input("Enter text here:")
# if text=="Hi":
#     print("Wellcome")


# number=int(input("Set number:"))
# if 0<number<=100:
#     print("Correct number")
# else:
#     print("Incorrect number")

#
# text=(input ("What is your name?:"))
# sub=' '
# sub2="."
# if sub in text:
#     print("Привет " + str(text) + " в вашем имени " + str(text.count(sub,0,len(text)))+" пробел")
# elif sub2 in text:
#     print("Привет " + str(text) + " в вашем имени " + str(text.count(sub2, 0, len(text))) + " точки")
# else:
#     print("Привет " + str(text) + " в вашем имени нет точек и пробелов")


# a=179
# b=971
# c = math.sqrt(a**2+b**2)
# print (str(c))

# num = input("Введите число:")
# if len(num)==2:
#     print ("Ваше число содержит "+ str(num[0])+" дестяков")
# elif len(num)==3:
#     n=int(num)
#     a=n%10
#     n=n//10
#     b=n%10
#     n=n//10
#     c=n%10
#     print("Cумма цифр числа " + str(a+b+c))



# num=input("print number:")
# n=int(num)
# if n%2==0:
#     print(str(n+2))
# else:
#     print(str(n+1))
def year_leap(a):
    if (a % 4 == 0,a % 100 != 0) or a % 400 == 0:
        print("YES, you birth year is a leap-year")
    else:
        print("NO, you birth year is not a leap-year")

m = input("print your birth year:")
y = year_leap(int(m))
print(y)





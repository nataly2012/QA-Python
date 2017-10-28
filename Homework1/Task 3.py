year = input("Please type your year of birth here:")
year = int(year)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES, you birth year is a leap-year")
else:
    print("NO, you birth year is not a leap-year")

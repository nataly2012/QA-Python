#Task 1.1

string=input("Print something here:")
if string.isdigit():
    print("You " + str(string) + " has numbers")
else:
   print("You " + str(string) + " has letters")

# Task 1.2-1.3

text=(input ("What is your name?:"))
sub=' '
sub2="."
if sub in text:
    print("Привет " + str(text) + " в вашем имени " + str(text.count(sub,0,len(text)))+" пробел")
elif sub2 in text:
    print("Привет " + str(text) + " в вашем имени " + str(text.count(sub2, 0, len(text))) + " точки")
else:
    print("Привет " + str(text) + " в вашем имени нет точек и пробелов")



#Task 1.4

text="Homework"
print(text.center(100, ' '))

#Task 1.5

text2 = (input("Print text here:"))
print(text2.title())







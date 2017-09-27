a=input("a=")
a=int(a)
b=input("b=")
b=int(b)
c=input("c=")
c=int(c)
if a + b > c and a + c > b and b + c > a:
	print("Yes, triangle exists ")
else:
	print("No, triangle does not exist")
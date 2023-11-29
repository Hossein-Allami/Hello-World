a = int(input("Enter first number a:"))
b = int(input("Enter second number b:"))
c = int(input("Enter third number c:"))


if a + b > c and a + c > b and b + c > a:
    print("Yes, it is")
else:
    print("No, it is not")

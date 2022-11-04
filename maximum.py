x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=int(input("Enter third number :"))
print("The maximum number is : ", end="")
if x<=y>=z:
       print(y)
elif y<=x>=z:
       print(x)
elif y<=z>=x:
       print(z)

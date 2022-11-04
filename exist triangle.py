print("This program tells you if suggested triangle could be existed or not!")
print("Type sides of triangle: ")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if x+y>z and x+z>y and y+z>x:
       print("EXISTS!")
else:
       print("Oops..DOES NOT EXIST!")

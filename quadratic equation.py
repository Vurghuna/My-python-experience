from math import sqrt
a = float(input("Insert a = "))
b = float(input("Insert b = "))
c = float(input("Insert c = "))

D = b**2 - 4*a*c

if D>0:
       x1 = (-b + sqrt(D))/(2*a)
       x2 = (-b - sqrt(D))/(2*a)
       print("Results: x1 = %.2f; x2 = %.2f" % (x1,x2))
elif D == 0:
       x = -b/(2*a)
       print("x = %.2f " % x)
else:
       print("No roots exist!")

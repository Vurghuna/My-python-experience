a = int(input("Enter first number :"))              
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

print("The minimum number is :", end ="")
if a<=b<=c:
        print(a)
elif b<=a<=c:
       print(b)
elif c<=b<=a:
       print(c)
        

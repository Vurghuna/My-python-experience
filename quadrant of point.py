x = float(input("Insert coordinate of point x :"))
y = float(input("Insert coordinate of point y :"))

if x>0 and y>0:
       print("This point is in first quadrant")
elif x<0 and y>0:
       print("This point is in second quadrant")
elif x<0 and y<0:
       print("This point is in third quadrant")
elif x>0 and y<0:
       print("This point is in forth quadrant")
elif x == 0 and y == 0:
       print("This is point of origin")
elif x == 0:
       print("This point is on y axis")
elif y == 0:
       print("This point is on x axis")

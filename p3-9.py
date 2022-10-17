from cmath import sin
h=int(input("enter the hight is :"))
a=int(input("enter the angle is :"))
pie=float(3.14)
angler=(pie/180)*a
l=(h/sin(angler))
print("ladder lanth is :",l)


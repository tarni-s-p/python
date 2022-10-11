from cmath import sqrt 
a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
c=int(input("enter the value of c :"))
de=float((b**2)-(4*a*c))
sol1=(-b+sqrt(de))/(2*a)
sol2=(-b-sqrt(de))/(2*a)
print("SOLUTION 1 IS :",sol1)
print("SOLUTION 2 IS:",sol2)

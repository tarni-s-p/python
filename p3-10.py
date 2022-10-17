a=int(input("enter the values of a is :"))
b=int(input("enter the values of b is :"))
c=int(input("enter the values of c is :"))

A= (a if(a > b and a > c) else b if(b > a and b > c) else c) 
print(A," is maximum")

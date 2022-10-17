w=int(input("enter the weight :"))
h=float(input("enter the height :"))
BMI=w/(h**2)
if BMI < 19:
    print("is underweight")
elif BMI > 25:
    print("is overweight")
else:
    print("is healthy")

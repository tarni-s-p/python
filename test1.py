#hrs = input("Enter Hours:")
#h = float(hrs)
#xx = input("Enter the Rate:")
#x = float(xx)
#if h <= 40:
 #	print( h  * x)
#elif h > 40:
#	print(40* x + (h-40)*1.5*x)*/
hrs = int(input("Enter Working Hours: "))
x = float(input("Enter rate hours: "))
if hrs <= 40:
 tax = float(hrs) * float(x)
 print(tax)
else:
 tax = float(40 * x + (hrs - 40) * 1.5 * x)
print(tax)
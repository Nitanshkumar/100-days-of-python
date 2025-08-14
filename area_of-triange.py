a=float(input("enter your first side"))
b=float(input("enter your second side"))
c=float(input("enter your third side"))

#calculate semi perimeter

s=(a+b+c)/2

#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
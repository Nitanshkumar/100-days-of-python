import cmath
a=float(input("enter your first side"))
b=float(input("enter your second side"))
c=float(input("enter your third side"))

#calculate discrimant
d=b**2 - (4*a*c)
4

#find two solutions 
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('the solutions are{0} and {1}'.format(sol1,sol2))
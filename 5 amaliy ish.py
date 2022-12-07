from math import*
x=17.421
y=10.365*10**-3
z=0.828*10**5

f =  ((y+(x-1)**(1/3))**(1/4))/(fabs(x-y)*(sin(z)**2)+tan(z))
print(f)

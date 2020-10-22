#Busqueda de newton
import matplotlib.pyplot as plt
import numpy as np

f=lambda x: x*x-np.sin(x)
f_1a=lambda x: 2*x-np.cos(x)
f_2a=lambda  x: 2+np.sin(x)

xi= 0.5
epsilon= 0.1
def Newton(xi,epsilon,f,f_1a,f_2a):
    xn=xi
    n=0
    while abs(f_1a(xn))>=epsilon:
        xn=xn-f_1a(xn)/f_2a(xn)
        n+=1
        print('Newton valor minimo:  \n','Valor en X= ',xn,', Valor en Y= ',f(xn))
        if n==10:
          break
    return xn

Newton(xi,epsilon,f,f_1a,f_2a)

a,b = 0,1
x = np.linspace(a, b, 11)
y=f(x)
plt.plot(x, y, 'r')
plt.grid(True)
plt.show()
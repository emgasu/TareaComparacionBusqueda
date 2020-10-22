# Busqueda Exhaustiva
from numpy import arange,sin
import matplotlib.pyplot as plt

def f(x):
  return (x*x)-sin(x)

x=arange(0.0,1.1,0.1)
array=[]
for x_ in x:
      array.append(f(x_))
      print("Valor en X = ",x_," Valor en Y = ",f(x_))

print(" El Minimo es ",min(array))

plt.plot(x,f(x),"red")
plt.grid(True)    


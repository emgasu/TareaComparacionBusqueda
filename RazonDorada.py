#Razon Dorada
import math
from numpy import arange,sin
import matplotlib.pyplot as plt
import numpy as np

def Graficacion(x1,y1):
    a,b = 0,1
    x = np.linspace(a, b, 11)
    f = (x*x)-sin(x)
    plt.figure(figsize=(6, 3))
    plt.plot(x, f, 'r')
    plotPunto(x1,y1)
    plt.grid()
    
    plt.show()


def f(x):
    return (x*x)-sin(x)


def f_RazonDorada():
    a = 0
    b = 1
    tau = 2 - 1.618033988
    epsilon = 1e-6
    cont = 0
    array = []

    while(True):
        # Calcular alpha1 y alpha2
        alpha1 = a*(1 - tau) + b*tau
        alpha2 = a*tau + b*(1 - tau)

        # Calcular f(alpha1) y f(alpha2)
        f_alpha1 = f(alpha1)
        f_alpha2 = f(alpha2)
        
        if(f_alpha1 > f_alpha2):
            a = alpha1
        else:
            b = alpha2       

        cont = cont + 1
        array.append([cont, alpha1, f_alpha1])
        print("Iteracion =",cont,"Valor en X = ",alpha1," Valor en Y = ", f_alpha1)

        if(np.abs(f_alpha1 - f_alpha2) < epsilon):
            print("------------------------         RESULTADO         -------------------------------")
            print("Iteracion =",cont,"Valor en X = ",alpha1," Valor en Y = ", f_alpha1)
            x1=alpha1
            y1=f_alpha1
            break      
    Graficacion(x1,y1)   
    return array,x1,y1



def plotPunto(x1,y1):
    plt.plot(x1,y1, marker="x", color="blue")

f_RazonDorada()






  
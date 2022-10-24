import math

import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
from decimal import getcontext

#polinom helyettesitesi erteke

def poly(c, A):
    res, p = 0, 1
    for a in A[::-1]:
        res += a*p
        p*=c

    return res

def horner (c, A):
    res = 0

    for a in A:
        res += res * c + a

    return res

def yValue (L, xS, xF, step):
    x = xS
    while x < xF:
        print(x, horner(x, L))
        x+= step

def fuggveny_abrazolas():
    X = np.linspace(-200,200,300,endpoint = True)
    F1 = horner(X, [1,-4,3])
    F2 = horner(X, [2, 7, 7])

    plt.plot(X, F1, label="F1")
    plt.plot(X, F2, label="F2")

    plt.axvline(x=0, c = "lightgray")
    plt.axhline(y=0, c = "lightgray")

    plt.show()

def my_sin(z, p = 50):
    getcontext().prec = p
    z = Decimal(math.radians(z))

    temp = Decimal(0)

    for x in range(1000,0,-2):
        a = (x+2)*(x+3) - z*z
        b = x * (x+1) * (z*z)
        temp = b/(a+ temp)

    temp = (z*z) / (2*3 - z*z +temp)

    return z/(1+ temp)

def main():

    #fuggveny_abrazolas()
    print(my_sin(Decimal(math.radians(60))))
    return 0

if __name__ == '__main__':
    main()
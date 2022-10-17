from math import gcd
from fractions import Fraction
from decimal import Decimal, getcontext

def euklidesz(a,b):

    if not isinstance(a,int) or not isinstance(b,int):
        return 'Hibas bemenet'

    a = abs(a)
    b = abs(b)

    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return  b

def euklidesz_rekurziv(a,b):
    a = abs(a)
    b = abs(b)

    r = a % b
    if r == 0:
        return b
    return euklidesz_rekurziv(b, r)

def irreducibilis(a,b):
    temp = euklidesz_rekurziv(a,b)
    return (a // temp, b // temp)

def auxRacionalis(k):
    for j in range(1, k+1):
        if k % 2 == 1:
            print((j, k+1-j), end=" ")
        else:
            print((k+1-j,j), end=" ")
    print()

def racionalisL(n):
    L = []
    for k in range (1,n+1):
        for j in range(1, k+1):
            L+=[(j,k+1-j)]
            n = n - 1
            if n == 0:
                return L
    print()

def racionalis1(n):
    for k in range (1,n+1):
        auxRacionalis(k)

def nextRac(x, y):
    nrx = (2* (x//y)+1) * y - x
    nry = y

    g = gcd(nrx,nry)

    return (nry //g, nrx //g)

def racionalis3(n):
    if n < 1:
        return []

    x, y = 1, 1
    L= [(x,y)]

    for i in range (1, n):
        x, y = nextRac(x, y)
        L += [(x,y)]

    return L

def nextRacFrac(r):
    x, y = r.numerator, r.denominator

    temp = 2 * (x//y) + 1

    res = Fraction(temp, 1) - Fraction(x, y)

    return Fraction(res.denominator, res.numerator)

def racionalis4(n):
    if n < 1:
        return []

    x = Fraction(1, 1)
    L= [x]

    for i in range (1, n):
        x = nextRacFrac(x)
        L += [x]

    return L

def lancT(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return 'Hibas bemenet!'

    tAlak = x / y
    L = []

    while True:
        temp = x // y
        L+=[temp]
        r = x - temp * y
        if r == 0:
            break;
        x = y
        y = r
    return (tAlak, L)

def lancTortGyokKetto(p):
    getcontext().prec = p
    temp = Decimal('0')

    for i in range(0,500):
        temp = 1/(2+temp)

    return 1+temp

def lancTortPi(p):
    getcontext().prec = p

    temp = Decimal('0')

    for x in range(1000,0,-1):
        a = x * x
        b = 2 * x + 1
        temp = a / (b + temp)

    return 4 / (1 + temp)

def lancTortE(p):
    getcontext().prec = p

    temp = Decimal('1')

    for i in range(1000,0,-1):
        temp = i + (i/temp)

    return 2 + (1/temp)

def lancTortPhi(p):
    getcontext().prec = p

    temp = Decimal('0')

    for x in range(0,500):
        temp = 1/(1+temp)

    return 1+temp

def hazi_feladat_irreducibilis(n):
    for k in range(1,n+1):
        for j in range(1,k+1):
            a, b = j, k+1-j
            a1, b1 = irreducibilis(a,b)
            if a == a1 and b == b1:
                print((a, b), end=' ')

def main():
    #print(euklidesz(61,47))
    #print(euklidesz_rekurziv(-32,-76))
    #print(nextRac(4,3))"""
    #print(lancT(41,11))
    #a, b=irreducibilis(26,8)
    #print(a, "/", b)
    #print(auxRacionalisL(5))
    #racionalis1(5)
    #hazi_feladat_irreducibilis(5)
    #print(racionalisL(7))
    #print(nextRac(5,2))
    #print(racionalis3(10))
    #print(racionalis4(10))
    #print(lancT(89,55))
    #print(lancTortGyokKetto(30))
    #print(lancTortPi(100))
    print(lancTortE(100))
    #print(lancTortPhi(100))

    return 0


if __name__ == '__main__':
    main()
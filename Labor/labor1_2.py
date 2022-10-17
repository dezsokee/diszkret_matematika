import math

def osszeg(a, b):
    return a + b

def kulonbseg(a, b):
    return a - b

#tuple - a fuggveny visszateresi erteke, 6 elemmel
def muveletek(a ,b):
    return a + b, a - b, a * b, a / b, a % b, a // b

def mainMuveletek1():
    a = int(input("a="))
    b = int(input("b="))

    eredmeny = muveletek(a, b)

    print("Osszeg: ", eredmeny[0])
    print("Kulonbseg: ", eredmeny[1])
    print("Szorzat: ", eredmeny[2])
    print("Hanyados: ", eredmeny[3])
    print("Maradeka az osztalynak: ", eredmeny[4])
    print("Egesz resze az osztasnak: ", eredmeny[5])

def mainMuveletek2():
    a = float(input("a="))
    b = float(input("b="))

    x, y, c, d, e, f = muveletek(a, b)

    print("Osszeg: ", x)
    print("Kulonbseg: ", y)
    print("Szorzat: ", c)
    print("Hanyados: ", d)
    print("Maradeka az osztalynak: ", e)
    print("Egesz resze az osztasnak: ", f)

def myMax1(a, b):
    if (a > b):
        return a
    return b

def myMax2(a, b):
    if (a > b):
        print(a)
    else:
        print(b)

def myMax3(a, b):
    if (a > b):
        print(a)
        return
    print(b)

def ketto_hatvanyai(n):
    for i in range(n):
        print(2, "^", i," = ", 2**i, end="\n")

def x_hatvanyai(x, n):
    kitevo = 0
    while kitevo <= n:
        print(kitevo, x**kitevo)
        kitevo = kitevo + 1

def mainHatvanyX():
    x = int(input("x="))
    n = int(input("n="))
    x_hatvanyai(x, n)

def negyzetgyok():
    n = int(input("n="))
    for i in range(n):
        x = float(input("x="))
        print("Negyzetgyok: ", math.sqrt(x))

#kijelentem hogy mindig a max a legnagyobb es ha kapunk nala nagyobbat akkor lecsereljuk
def legnagyobb(n):
    max = float(input("x="))
    for i in range(n-1):
        #print("Reszmaxiumum: ", max)
        x = float(input("x="))
        if x > max:
            max = x
    print("A legnagyobb szam: ", max)

def elojel(x):
    if (x > 0):
        return "Pozitiv"
    if x == 0:
        return "Nulla"
    else:
        return "Negativ"

def elojel1(x):
    if (x > 0):
        return "Pozitiv"
    elif x == 0:
        return "Nulla"
    else:
        return "Negativ"

def myCeil(x):
    if x < 0:
        return int(x)
    else:
        b = int(x)
        if (float(b) == x):
            return b
        else:
            return b+1

def main():
    #print(osszeg(17, 15))
    #print(kulonbseg(17, 15))
    #mainMuveletek1()
    #mainMuveletek2()
    #myMax3(11, 8)
    #ketto_hatvanyai(5)
    #x_hatvanyai(5,3)
    #mainHatvanyX()
    #negyzetgyok()
    #legnagyobb(5)
    #print(elojel(0))
    print(myCeil(-7.5))

if __name__ == "__main__":
    main()
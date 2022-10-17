import math

def feladat1_1 (a,b):
    #muveletek az argumentumokkal
    print("A", a, "es", b, "szam osszege:", a+b)
    print("A", a, "es", b, "szam kulonbsege:", a-b)
    print("A", a, "es", b, "szam szorzata:", a*b)
    print("A", a, "es", b, "szam hanyadosa:", a/b)
    print("A", a, "es", b, "szam osztasi maradeka:", a%b)

def feladat1_2 (a, b):
    # maximum es minimum kereses
    if (a > b):
        print("A", a, "a maximum es a", b, "a minimum")
    else:
        print("A", b, "a maximum es a", a, "a minimum")

def feladat1_3 ():
    #elso foku egyenlet gyoke

    a = 7
    b = 5
    z = 0

    print(a, "* x  +", b, "=", z)

    x = -b/a

    print("x=", x)

def feladat1_4(a):
    #egy szam modulusza

    if (a >= 0):
        return a
    else:
        return -a

def feladat1_5(a):
    #egy szam elojele

    if (a >= 0):
        print("Pozitiv elojelu a", a, "szam")
    else:
        print("Negativ elojelu a", a, "szam")

def feladat1_6(a):
    #egy valos szam also hatara
    print("A", a, "szam also hatara", int(a))
    #egy valos szam felso hatara
    print("A", a, "szam felso hatara", int(a)+1)

def feladat1_7(a, b, c):
    #masodfoku fuggveny gyokeinek meghatarozasa

    delta = b*b-(4*a*c)
    if (delta < 0):
        print("Nincs valos gyoke az egyenletnek")
    else:
        gyok_delta = math.sqrt(delta)
        print("A",a,"x^2 +",b,"x +",c , "masodfoku egyenlet gyokei:", (-b + gyok_delta/(2 * a)), "es", (-b - gyok_delta/(2 * a)))

def feladat1_8():
    #hany byte szukseges k bit eltarolasahoz

    k = int(input("Add meg a k szamot!\n"))

    if (k % 8 == 0):
        print("A", k, "szam eltarolasahoz", k/8, "byte szukseges")
    else:
        print("A", k, "szam eltarolasahoz", int(k / 8) + 1, "byte szukseges")

def feladat2():
    n = int(input("Adj meg egy n termeszetes szamot!\n"))

    #az elso n termeszetes szam kiirasa
    for i in range(n):
        print(i + 1, " ")

    #az elso n paros teremeszetes szam
    for i in range(n + 1):
        if (i % 2 == 0):
            print(i, " ")

    #az elso n darab paros szam tombbe tarolva
    paros_lista = []
    db = 0
    i = 0
    while (db < n):
        print(i, " ")
        paros_lista.append(i)
        i = i + 2
        db = db + 1

    #az elso n darab paratlan szam tombbe tarolva
    paratlan_lista = []
    db = 0
    i = 1
    while (db < n):
        print(i, " ")
        paratlan_lista.append(i)
        i = i + 2
        db = db + 1

    #n-ig a negyzetszamok
    for i in range(n):
        if (i * i <= n):
            print(i * i, " ")

    #az elso n darab negyzetszam tombbe tarolva
    negyzet_lista = []
    db = 0
    i = 1
    while (db < n):
        print(i * i, " ")
        negyzet_lista.append(i * i)
        i = i + 2
        db = db + 1

    #az elso n szam osszege
    ossz = 0

    for i in range(n):
        ossz = ossz + i

    print("Az elso", n, "szam osszege", ossz)

    #az elso n szam szorzata
    szor = 0

    for i in range(n):
        szor = szor * i

    print("Az elso", n, "szam szorzata", szor)

def feladat3():
    n = int(input("Az n erteke:"))

    for i in range(n):
        print("2^", i, "=", 2**i, end=";")

def feladat4():
    n = int(input("Az n erteke:"))
    x = int(input("Az x erteke:"))

    for i in range(n):
        print(x, "^", i, "=", x**i, end=";")

def feladat5():
    n = int(input("Az n erteke:"))

    for i in range(n):
        x = int(input())
        print(x ** 2)

def feladat6():
    n = int (input("Hany szamot szeretnel?\n"))
    max = int (input("Az 1. szam: \n"))
    for i in range (n-1):
        print("A", i+2, ". szam: ")
        x = int(input())
        if ( x > max):
            max = x
    print("A legnagyobb szam: ", max)

def feladat7():
    n = int (input("Hany szamot szeretnel?\n"))
    max = int (input("Az 1. szam: \n"))
    ssz = 1
    for i in range (n-1):
        print("A", i+2, ". szam: ")
        x = int(input())
        if ( x > max):
            max = x
            ssz = i+2
    print("A legnagyobb szam: ", max, " es a ", ssz, ". helyen talalhato.")

def feladat8():
    n = int(input("Hany szamot szeretnel?\n"))
    ossz = 0

    for i in range(n):
        x = int(input())
        ossz = ossz + x

    print("A szamok osszege: ", ossz)

def feladat9():
    n = int(input("Hany szamot szeretnel?\n"))
    szor = 1

    for i in range(n):
        x = int(input())
        szor = szor * x

    print("A szamok szorzata: ", szor)

def feladat10():
    n = int(input("Add meg az n szamot!\n"))
    db = 0
    hat = 25
    for i in range (n):
        if ((i % 10 == 5) or (i % 5 == 0)):
            db = db + 1
    print(db)

def main():
    a = -17
    b = 12
    c = 1.5

    """feladat1_1(a, b)
    feladat1_2(a, b)
    feladat1_3()
    print("A", a, "szam abszolut erteke:", feladat1_4(a))
    feladat1_5(b)
    feladat1_6(c)
    feladat1_7(-1,3,4)
    feladat1_8()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()
    feladat9()"""
    feladat10()

if __name__ == "__main__":
    main()
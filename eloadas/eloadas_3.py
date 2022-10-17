from time import time

def beolvasFloat(n):
    L=[]

    try:
        for i in range(n):
            L+=[float(input("elem= "))]
    except:
        print("Hibas kimenet")

def myPowLin (x,n):
    res = 1
    st = time()

    for i in range (n):
        res *= x

    fs = time()
    print("Futasi ido: ", fs-st)

    print(res)

def gyorshatvany(x,n):
    res = 1

    st = time()

    while(n!=0):
        if n % 2 == 1:
            res *= x
        n = n // 2
        x = x * x

    fs = time()

    print("Futasi ido: ", fs-st)
    print(res)

def gyorsHatvanyRekurziv(x,n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * gyorsHatvanyRekurziv(x*x, n // 2)
    return gyorsHatvanyRekurziv(x * x, n // 2)

def honapok():
    hL = ['jan', 'feb', 'mar']
    homL = [-5,7,5]
    resL = []
    teliHo = hL[0:2]

    for i in range(3):
        if homL[i] < 0 and hL[i] in teliHo:
            resL = resL + [hL[i]]

    print(resL)

def beolvas():
    inf = open('homerseklet.txt', 'rt')
    L = []

    while True:
        temp = inf.readline()
        if not temp: break
        temp = temp.strip('\n')
        honap, homerseklet = temp.split(' ')
        L+=[(honap,homerseklet)]

    inf.close()
    print(L)

def myGyorsHatvany(x, n):
    res = 1
    db = 0

    while n != 0:
        if n % 2 == 1:
            res = res * x
            db = db + 1
        n = n // 2
        x = x * x
        db = db + 1

    return res, db

def main():
    #beolvasFloat(5)
    #myPowLin(2,6)
    #gyorshatvany(2,6)
    #print(gyorsHatvanyRekurziv(2,3))
    #honapok()
    beolvas()
    """a, b = myGyorsHatvany(2,1023)
    print(a, b)"""

    return 0

if __name__ == "__main__":
    main()
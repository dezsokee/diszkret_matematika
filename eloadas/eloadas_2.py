from math import factorial

def kisbetu(x):
    if 'a' <= x <= 'z':
        return True
    else:
        return False

def negyzetszam(x):
    y = int(x ** 0.5)
    if float(y * y) == x:
        return True
    else:
        return False

def osztok_szama(n):
    if n <= 0:
        print("Helytelen bemenet")
        return

    db = 0
    i = 2

    while i <= n//2:
        if n % i == 0:
            db += 1
            print(i, end=' ')
        i += 1
    print("\n")

    return db

def faktorialis (x):
    res = 1

    for i in range(1, x+1):
        res *= i

    return res

def rekurziv_fackotiralis(x):
    if x == 0:
        return 1
    else:
        return x * rekurziv_fackotiralis(x-1)

def nulla_faktorialis(n):
    res = 0
    while n > 0:
        temp = n // 5
        res += temp
        n = temp

    return res

def tupple(x,y):
    return x+y, x-y, x*y, x/y, x//y, x%y

#diszkret logaritmus problema
def modN():
    a = int(input('a: '))
    n = int (input('modulus: '))
    for i in range (1,n):
        print(pow(a, i, n))

def main():
    ##print(kisbetu('C'))
    ##print(negyzetszam(15))
    ##print(osztok_szama(16))
    #print(faktorialis(5))
    #print(rekurziv_fackotiralis(5))
    #print(nulla_faktorialis(91))
    """for elem in tupple(10,5):
        if isinstance(elem, float):
            print(elem)"""
    modN()

    return ""

if __name__ == "__main__":
    main()
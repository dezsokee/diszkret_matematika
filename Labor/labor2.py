import math

def szamparBeolvas():
    temp = input("x y: ")
    if temp == "":
        return ""
    temp = temp.split()
    try:
        t1, t2 = temp
        x = int(t1)
        y = int(t2)
    except:
        print("Hibas bemenet!")
        return -1

    return x, y

def mainPow():
    while True:
        res = szamparBeolvas()
        if res == "":
            return
        elif res == -1:
            continue
        x, y = res
        res, db = gyorshatvany(x, y)
        db1 = szorSzam(y)
        print("Szorzasok szama:", db-1, db1, "eredmenye: ", res)

#a szorzasok szama meghatarozhato a hatvanyertek kiszamitasa nelkul
def szorSzam(y):
    temp = bin(y)
    db = len(temp) - 2 + szamolEgy(temp) - 1
    return db

def szamolEgy(x):
    db = 0
    for t in (x):
        if t == "1":
            db += 1
    return db

def gyorshatvany(x, n):
    res, szor = 1, 0

    while n != 0:
        if n % 2 == 1:
            res *= x
            szor +=1
        x *= x
        szor += 1
        n = n // 2

    return res, szor

def ellenorzes3():
    n = input("n=")
    n = int(n)
    p = 1
    for i in range(1,n+1):
        print(p, end=" ")
        p *= 3

def ellenorzes6B(n):
    for i in range(1,n+1):
        print(pow(2,i), end=" ")

def ellenorzes6A():
    n = int(input("n="))
    for i in range(1,n+1):
        print(i*i*i, end=" ")

def proba():
    for j in range (5):
        print(5, end=" ")

def ellenorzes6C():
    temp = 0
    n = int(input("n="))
    for i in range(1,n+1):
        for j in range(i):
            print(i, end=" ")
            temp +=1
            if temp == n:
                return

def ellenorzes6D():
    n = int(input("n="))
    db = 0
    for i in range(1,n+1):
        for j in range(i):
            print(1, end=" ")
            db +=1
            if db == n:
                return
        for j in range (i):
            print(0, end=" ")
            db +=1
            if db == n:
                return

def ellenorzes6E():
    n = int(input("n="))
    for i in range(1,n+1):
        if i % 2 == 0:
            print(0, end=" ")
        else:
            print(2**(i//2), end=" ")

def ellenorzes6G():
    n = int(input("n="))
    for i in range(1,n+1):
        if i % 2 == 0:
            print(0, end=" ")
        else:
            print(2**(i//2), end=" ")

def ellenorzes6F():
    n = int(input("n="))
    temp = 0
    for i in range(1,n+1):
        if (i%2!=0):
            print(i, end=" ")
            temp +=1
            if temp == n:
                return
        else:
            print(i, end=" ")
            temp += 1
            if temp == n:
                return
            print(i, end=" ")
            temp += 1
            if temp == n:
                return

def ellenorzes6H():
    n = int(input("n="))
    p = 2
    temp = 0
    print(p, end=" ")
    for i in range(1,n+1):
        p = p * p
        print(p, end=" ")
        temp += 1
        if temp == n:
            return

def fibonacci():
    n= int(input("n="))
    a, b = 0,1
    print(a, b, end=" ")
    for i in range(n-1):
        c, a = a + b, b
        b = c
        print(c, end=" ")
    #print(c)

def digit_number(nr):
    temp = int(math.log(nr, 10))
    return temp + 1

def bit_number(nr):
    temp = int(math.log(nr, 2))
    return temp + 1

def factorial_number(nr):
    temp = 0

    for i in range(1,nr+1):
        temp += math.log(i, 10)

    return int(temp) + 1

def maxFactDigit(k):
    n = 1
    while True:
        temp = factorial_number(n)
        if temp >= k:
            return n-1
        n+=1

def main():
    #ellenorzes3()
    #ellenorzes1()
    #proba()
    #ellenorzes4_()
    #ellenorzes4()
    #ellenorzes5()
    fibonacci()
    #print(factorial_number(10))
    #print(maxFactDigit(5))
    #ellenorzes6C()
    #ellenorzes6H()

    return 0

if __name__ == '__main__':
    main()

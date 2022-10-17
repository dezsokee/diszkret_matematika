def feladat_1():
    ossz, szor = 0, 1
    list=[]

    print("Add meg hany szamot szeretnel beolvasni!")
    n = int(input())

    min = int(input())
    max = min
    list = list + [min]
    minPoz,maxPoz = 1, 1

    parosSz,negyzetSz = 0, 0

    #beolvasas
    for i in range (n-1):
        x = int(input())
        list = list + [x]
        if x > max:
            max = x
            maxPoz = i + 2

        if x < min:
            min = x
            minPoz = i + 2

    #kiiratas, osszeg, szorzat, paros szamok szama
    for i in range(n):
        print(list[i], end=" ")
        ossz = ossz + list[i]
        szor = szor * list[i]
        if 0 == list[i] % 2:
            parosSz = parosSz + 1
        y = int(list[i] ** 0.5)
        if float(y * y) == list[i]:
            negyzetSz = negyzetSz + 1

    print("\nA szamok osszege:", ossz, "es szorzata:", szor)
    print("\nA szamok kozul a legkisebb:", min, ",pozicioja:", minPoz, "illetve legnagyobb:", max, "pozicioja:", maxPoz, "\n")
    print(parosSz, "darab paros szam van a listaban\n")
    print("A listaban megadott szamok atlaga:\n", ossz/n)

    print("A paros szamok es poziciojuk:")
    for i in range (n):
        if 0 == list[i] % 2:
            print(list[i], "-", i+1, end=" ")

    print("\nA nagyzetszamok es poziciojuk:")
    for i in range(n):
        y = int(list[i] ** 0.5)
        if float(y * y) == list[i]:
            print(list[i], "-", i+1, end=" ")

def fugv(maxH, inf):
    temp = inf.readline()
    temp = temp.split('\t')
    temp = temp[1:]
    l1 = []
    for elem in temp:
        l1 += [int(elem)]

    maxH += [l1]
    return maxH

def homerseklet():
    inf = open('homerseklet.txt', 'rt')
    honapok = inf.readline().split()
    varosok = []
    maxH, minH = [], []

    while True:
        temp = inf.readline()
        if not temp:
            break
        temp = temp.strip()
        varosok += [temp]
        fugv(maxH, inf)
        fugv(minH, inf)
        inf.readline()

    print(honapok)
    print(varosok)
    print(maxH)
    print(minH)

    inf.close()

    print("A legkisebb min max atlaghomersekletek varosonkent:\n")
    k = 0
    for i in maxH:
        min = i[0]
        for j in i:
            if j<min:
                min = j
        print(varosok[k]," - ", min, end="\n")
        k = k + 1

    print("Azok a honapok amikor a min atlaghomerseklet kisebb volt mint 0 varosonkent:\n")
    k = 0

    for i in minH:
        print(varosok[k],":")
        q = 0
        for j in i:
            if j < 0:
                print(honapok[q])
            q = q + 1
        k = k + 1

    print("Azok a honapok amikor minden varosban kisebb volt a min atlaghomerseklet mint 0: \n")

    db = [0] * 12

    for i in minH:
        q = 0
        for j in i:
            if j < 0:
                db[q] = db[q] + 1
            q = q + 1

    i = 0
    while i != 12:
        if db[i] == 7:
            print(honapok[i], end=" ")
        i = i + 1

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

def bina(x):
    bin_db = 0

    while x != 0:
        x //= 2
        bin_db += 1

    print(bin_db, " szamjegybol all a szam kettes szamrendszerben!")

def main():
    #feladat_1
    #homerseklet()
    """res, szor = gyorshatvany(2,3)
    print(res, " - ", szor)"""
    bina(7)
    #mainPow()
    return 0

if __name__ == "__main__":
    main()
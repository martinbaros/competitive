#T the number of test cases to solve
s = open("output.txt", "w")
all = []
with open("input-scheduler-facc.txt","r") as f:
    for line in f:
        line = line.strip()
        line = line.split(" ")
        all.append(line)


def findCombinationsUtil(arr, index, num,
                              reducedNum,ch):
    global spravne
    if (reducedNum < 0):
        return;
    if (reducedNum == 0):
        new = []
        for i in range(index):
            new.append(arr[i])
        print(len(new))
        print(ch)
        if len (new) == ch:
            spravne.append(new)
        return;
    prev = 1 if(index == 0) else arr[index - 1];
    for k in range(prev, num + 1):
        arr[index] = k;
        findCombinationsUtil(arr, index + 1, num,
                                 reducedNum - k,ch);

def findCombinations(n,ch):
    arr = [0] * n;
    findCombinationsUtil(arr, 0, n, n,ch);


t = int(all[0][0])
print(t)
actual = 1
case_n = 1
print(len(all))
while actual < len(all):
    #case-starting

    n = int(all[actual][0])
    k = int(all[actual][1])
    m = int(all[actual][2])
    priem = m//k
    zvyskova = priem + m%k
    #best = []

    case = []
    c_t = []
    best_t = []
    best_c = []
    for i in range(n):
        actual+=1
        startup = int(all[actual][0])
        speed = int(all[actual][1])
        real = startup+(speed*priem)
        c_t.append(real)
        case.append([startup,speed])

        if len(best_t) < k:
            best_t.append(real)
            best_c.append([startup,speed])
        elif real < max(best_t):
            ind = best_t.index(max(best_t))
            best_t[ind] = real
            best_c[ind] = [startup,speed]
        else:
            print("nope")
        print(actual)
    print(n,k,m)
    print(best_c, best_t)
    actual+=1
    spravne = []
    special = False
    if m < k:
        special = True
    else:
        findCombinations(m,k);

    print(spravne)
    poradie = {}

    for x,y in best_c:
        poradie[f"{x} {y}"] = y
    vysledok = -2


    if special:
        for x,y in best_c:
            poradie[f"{x} {y}"] = x
        vysledok = -2
        full = []
        konec = []
        for x in sorted(poradie, key = poradie.get):
            letd = x.split(" ")
            full.append(int(letd[0])+(int(letd[1])*1))
        print(min(full))
        for i in range(m):
            if len(full)>0:
                konec.append(min(full))
                full.pop(full.index(min(full)))
        print(konec)
        print("here")

        if vysledok == -2:
            vysledok = max(konec)
        elif max(konec) < vysledok:
            vysledok = max(konec)
    for i in range(len(spravne)):
        for x,y in best_c:
            poradie[f"{x} {y}"] = y
        vysledok = -2
        full = []

        zoz = sorted(spravne[i],reverse = True)
        i = 0
        for x in sorted(poradie, key = poradie.get):
            letd = x.split(" ")
            full.append(int(letd[0])+(int(letd[2])*zoz[i]))
            i+= 1
        print(full)
        print("here")
        print(max(full))
        if vysledok == -2:
            vysledok = max(full)
        elif max(full) < vysledok:
            vysledok = max(full)
    print(vysledok)
    print(f"Case #{case_n}: {vysledok}",file = s)
    case_n+=1
s.close()

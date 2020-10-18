def nsd(a,b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("NIECO JE ZLE")
        return False
    else:
        if b == 0:
            return False
        else:
            while a>0:
                if a < b:
                    a,b = b,a
                a -= b

            return b

inp = open("input_file.txt", "r")
s = open("output_file.txt", "w")
t = int(inp.readline())
print(t)

for i in range(1, t+1):
    zle = inp.readline().strip()
    omg = zle.split(" ")
    print(i)
    n = int(omg[0])
    l = int(omg[1])
    nieco = inp.readline().strip()
    medzi = nieco.split(" ")
    case = []
    for c in medzi:
        case.append(int(c))
    print(case)

    poradie = []
    vsetky = []
    for l in range(l-1):
        delitel = nsd(case[l],case[l+1])
        if l == 0:
            poradie.append(case[l]//delitel)
        if l == 1:
            poradie.append(poradie[1])
            poradie[1] = case[l]//delitel

        vsetky.append(case[l]//delitel)
        vsetky.append(case[l+1]//delitel)
        poradie.append(case[l+1]//delitel)

    #vyradovanie
    vsetky.sort()
    q = 0
    while q < len(vsetky):
        numero = vsetky[q]
        for p in range(vsetky.count(numero)-1):
            vsetky.remove(numero)
        q+=1
    slovnik = {}
    for r in range(26):
        slovnik[vsetky[r]] = chr(65+r)
    sprava = ""
    for cislo in poradie:
        sprava += slovnik[cislo]

    print("Case #{}: {}".format(i, sprava), file=s)

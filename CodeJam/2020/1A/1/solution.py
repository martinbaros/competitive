def spocitaj(matica,r,c):
    level = 0
    for k in range(r):
        for p in range(c):
            if matica[k][p] != "x":
                level += matica[k][p]
    return level

def priemer(matica, opacna, r, c, o, l):
    vysledok = 0
    pocet = 0
    print("prvok", matica[o][l])
    pocitadlo = 1
    while 1:
        if o - pocitadlo > -1:
            sused = matica[o-pocitadlo][l]
            if sused != "x":
                vysledok += sused
                pocet += 1
                break
            else:
                pocitadlo += 1
        else:
            break
    pocitadlo = 1
    while 1:
        if o+pocitadlo < len(matica)-1:

            sused = matica[o+pocitadlo][l]

            if sused != "x":
                vysledok += sused
                pocet += 1
                break
            else:
                pocitadlo += 1
        else:
            break
    pocitadlo = 1
    while 1:
        if l - pocitadlo > -1:

            sused = matica[o][l-pocitadlo]

            if sused != "x":
                vysledok += sused
                pocet += 1
                break
            else:
                pocitadlo += 1
        else:
            break
    pocitadlo = 1
    while 1:
        if l + pocitadlo < len(matica[o]):
            sused = matica[o][l+pocitadlo]
            print(sused, vysledok)
            if sused != "x":
                vysledok += sused
                pocet += 1
                break
            else:
                pocitadlo += 1
        else:
            break
    if pocet == 0:
        return matica[o][l]
    print(vysledok,pocet, o, l)
    return vysledok/pocet



t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    matica = []
    maximum = 0
    for k in range(1,r+1):
        case = [int(s) for s in input().split(" ")]
        if max(case) >= maximum:
            maximum = max(case)
        matica.append(case)
    opacna = []
    for o in range(c):
        opacna.append([])
    for o in range(r):
        for l in range(c):
            opacna[l].append(matica[o][l])
    level = 0
    tato_nejde = 0

    while tato_nejde < r*c:
        level += spocitaj(matica,r,c)
        zmeny = []
        tato_nejde = 0
        for o in range(r):
            for l in range(c):
                if (matica[o].count("x") <= len(matica[o])-1) and (opacna[l].count("x") <= len(opacna[l])-1):

                    if matica[o][l] <= priemer(matica, opacna, r, c, o, l):
                        zmeny.append([o,l])
                else:
                    tato_nejde += 1
        for pripad in zmeny:
            matica[pripad[0]][pripad[1]] = "x"
            opacna[pripad[1]][pripad[0]] = "x"
        print(matica)
        print(spocitaj(matica, r, c))



    print("Case #{}: {}".format(i, level))

def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]
    return seq

def check(inp, wanted):

    dlzka = 0
    case = [int(s) for s in inp.split(" ")]
    n = len(case)
    for i in range(n):
        minimum = case[i]
        j = i
        for k in range(i+1,n):
            if case[k] < minimum:
                minimum = case[k]
                j = k
        if i!= n-1:
            dlzka += (j-i+1)
        reverse(case, i, j)
    #print(wanted)
    #print(dlzka)
    print(wanted == dlzka)


def check_posibility(dlzka,chcene) -> bool:
    dlzka -= 1
    zoznam = [str(i+1) for i in range(dlzka+1)]
    i = 0
    koniec = dlzka
    zmena = 0
    smer = True
    kroky = koniec-i
    chcene -= kroky
    while koniec - i > 0:
        kroky = koniec-i
        #print("_AA_")
        #print(kroky)
        #print("NA")
        #print(chcene)
        #print("_AA_")
        if (i >= koniec) or (chcene < 0):
            return "IMPOSSIBLE"
        if chcene <= kroky:
            #print("endgame")
            #print(smer)
            if smer:
                zoznam = reverse(zoznam, i, i+chcene)
            else:
                zoznam = reverse(zoznam, koniec-chcene, koniec)
            return " ".join(zoznam)

        zoznam = reverse(zoznam, i, koniec)
        chcene -= kroky
        if smer:
            koniec -= 1
            smer = False
        else:
            i += 1
            smer = True
        #print(zoznam)
        #print("zmena")
        #print("ostava")
        #print(chcene)
    return "IMPOSSIBLE"




t = int(input())
for test in range(1, t+1):
    n,c = [int(s) for s in input().split(" ")]
    vysledok = check_posibility(n,c)
    if vysledok != "IMPOSSIBLE":
        check(vysledok,c)
    print("Case #{}: {}".format(test, vysledok))


"""
16
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
5 9
5 10
5 11
5 12
5 13
5 14
5 15
5 16
"""

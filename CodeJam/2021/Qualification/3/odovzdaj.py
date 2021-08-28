def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]
    return seq


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
        if (i >= koniec) or (chcene < 0):
            return "IMPOSSIBLE"
        if chcene <= kroky:
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
    return "IMPOSSIBLE"




t = int(input())
for test in range(1, t+1):
    n,c = [int(s) for s in input().split(" ")]
    vysledok = check_posibility(n,c)
    print("Case #{}: {}".format(test, vysledok))

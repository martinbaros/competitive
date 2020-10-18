t = int(input())  # read a line with a single integer
slovnik={}
final ={}
special = {}
def treba(vysledok):
    je = False
    todo = []
    pocty = []
    for qql in range(26):
        riesene = chr(qql+65)
        pocet = vysledok.count(riesene)
        if pocet > 1:
            je = True
            if riesene not in todo:
                todo.append(riesene)
                pocty.append(pocet)
    return [je,todo,pocty]



for q in range(10):
    slovnik[f"{q}"] = ""
for i in range(1, t+1):
    l = int(input())
    for f in range(10**4):
        cislo, text = [str(s) for s in input().split(" ")]
        if len(cislo) > len(text):
            text = text*2
        elif len(text) > len(cislo):
            cislo = cislo*2
        for i in range(len(cislo)):
            slovnik[cislo[i]] = slovnik[cislo[i]] + text[i]
    vysledok = ["0","0","0","0","0","0","0","0","0","0"]
    for c in slovnik:
        maxo = 0
        final[c] = ""
        for pql in range(26):
            pocet = slovnik[c].count(f"{chr(pql+65)}")
            if pocet > maxo:
                maxo = pocet
                vysledok[int(c)] = chr(pql+65)

    vynimky = []
    nic_viac = []
    while treba(vysledok)[0]:
        pismenka, pocty = treba(vysledok)[1], treba(vysledok)[2]
        ideme = pismenka[pocty.index(max(pocty))]
        #print(pismenka, pocty,ideme)
        indexy = []
        for waa in range(len(vysledok)):
            if vysledok[waa] == ideme:
                indexy.append(waa)
        #print(indexy)
        stat = []
        for ind in indexy:
            stat.append(slovnik[str(ind)].count(ideme))
        spravne = indexy[stat.index(max(stat))]
        nic_viac.append(spravne)
        vynimky.append(ideme)
        #print(nic_viac)

        for kazde in range(len(vysledok)):
            if kazde not in nic_viac:
                nenajdene = True
                while nenajdene:
                    maxo = 0
                    for nahodne_p in range(26):
                        forma = chr(nahodne_p+65)
                        pocet = slovnik[c].count(f"{forma}")
                        if forma not in vynimky:
                            if pocet > maxo:
                                maxo = pocet
                                vysledok[kazde] = forma
                                nenajdene = False
    konecne = ""
    for pismnekiksknd in vysledok:
        konecne+=pismnekiksknd
    print("Case #{}: {}".format(i, konecne))

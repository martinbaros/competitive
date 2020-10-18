t = int(input())  # read a line with a single integer
for I in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    tvar = []

    pismenka = []
    for i in range(c):
        tvar.append([])

    for i in range(r):
        case = str(input())
        for j in range(c):
            tvar[j].append(case[j])
            if case[j] not in pismenka:
                pismenka.append(case[j])


    final = ""
    while len(final)!=len(pismenka):
        ind = []
        not_ind = []
        for q in range(c):
            for pis in tvar[q]:
                if pis not in final:
                    hladane = pis
                    break
                else:
                    hladane = 0

            if hladane != 0:
                ostatok = 0
                for piq in final:
                    ostatok+=tvar[q].count(piq)
                if tvar[q].count(hladane) == r-tvar[q].index(hladane)-ostatok and (hladane not in not_ind):
                    if hladane not in ind:
                        ind.append(hladane)
                else:
                    if hladane in ind:
                        ind.remove(hladane)
                    if hladane not in not_ind:
                        not_ind.append(hladane)
        if len(ind) != 0:
            final += ind[0]
        else:
            final = -1
            break

    print("Case #{}: {}".format(I, final))

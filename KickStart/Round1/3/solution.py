def spocitaj(case):
    vysledok = []
    for i in range(len(case)-1):
        vysledok.append(case[i+1]- case[i])
    return vysledok

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    while k>0:
        rozdiely = spocitaj(case)
        if rozdiely.count(max(rozdiely)) <= k and max(rozdiely) > 1:
            poz = rozdiely.index(max(rozdiely))
            case.insert(poz+1, (case[poz]+case[poz+1])//2)
            k-=1
        else:
            k = 0
            break
    rozdiely = spocitaj(case)
    print("Case #{}: {}".format(i, max(rozdiely)))


t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n = int(input())
    starts = []
    ends = []
    asi = []
    c = False
    j = False
    mozne = True
    sprava = ""
    for k in range(1, n+1):
        start, end = [int(s) for s in input().split(" ")]
        starts.append(start)
        ends.append(end)
        asi.append("x")
    for r in range(min(starts), max(ends)+1):
        if r in ends:
            if ends.count(r) == 1:
                if asi[ends.index(r)] == "C":
                    c = False
                elif asi[ends.index(r)] == "J":
                    j = False
            elif ends.count(r) == 2:
                j = False
                c = False
            else:
                mozne = False
        if r in starts:
            if starts.count(r) == 1:
                if not c:
                    meno = "C"
                    c = True
                elif not j:
                    meno = "J"
                    j = True
                else:
                    meno = "x"
                    mozne = False
                asi[starts.index(r)] = meno
            elif starts.count(r) == 2:
                if (not c) and (not j):
                    poc = 0
                    vsetky = []
                    for nieco in starts:
                        if nieco == r:
                            vsetky.append(poc)
                        poc+=1
                    asi[vsetky[0]] = "C"
                    asi[vsetky[1]] = "J"
                    c = True
                    j = True
            else:
                mozne = False


    if not mozne:
        sprava = "IMPOSSIBLE"
    else:
        for pis in asi:
            sprava += pis
    print("Case #{}: {}".format(i, sprava))

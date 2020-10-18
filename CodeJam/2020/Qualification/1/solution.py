# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n = int(input())
    matica = []
    for k in range(1,n+1):
        case = [int(s) for s in input().split(" ")]
        matica.append(case)
    k = 0
    for f in range(n):
        k += matica[f][f]
    opacna = []
    for o in range(n):
        opacna.append([])
    r = 0
    c = 0
    riadok = False
    for o in range(n):
        riadok = False
        for l in range(n):
            opacna[l].append(matica[o][l])
            if matica[o].count(matica[o][l]) > 1:
                riadok = True
        if riadok:
            r += 1
    for o in range(n):
        stlpec = False
        for l in range(n):
            if opacna[o].count(opacna[o][l]) > 1:
                stlpec = True
        if stlpec:
            c += 1

    print("Case #{}: {} {} {}".format(i, k, r, c))

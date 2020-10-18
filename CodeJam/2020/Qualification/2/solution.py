
t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    case = str(input()) + "0"
    upravene = ""
    for r in range(len(case)):
        teraz = case[r]
        pocet = upravene.count("(") - upravene.count(")")
        if pocet < int(teraz):
            for o in range(abs(int(teraz)- int(pocet))):
                upravene+="("
        elif pocet > int(teraz):
            for o in range(abs(int(teraz)- int(pocet))):
                upravene+=")"
        upravene += teraz
    upravene = upravene[:len(upravene)-1]
    print("Case #{}: {}".format(i, upravene))

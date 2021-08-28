def solve(x,y,case):
    spolu = 0
    for i in range(1,len(case)):
        if case[i] == "?":
            case[i] = case[i-1]
        if case[i-1] == "C" and case[i] == "J":
            spolu += x
        elif case[i-1] == "J" and case[i] == "C":
            spolu += y
    return spolu


t = int(input())
for test in range(1, t+1):
    x,y,c = [str(s) for s in input().split(" ")]
    x = int(x)
    y = int(y)
    case = [str(s) for s in c]

    if len(case)>1 and (case[0] == "?" and case[1] == "?"):
        prve = case.copy()
        prve[0] = 'J'
        v1 = solve(x,y,prve)
        druhe = case.copy()
        druhe[0] = 'C'
        v2 = solve(x,y,druhe)
        vysledok = min(v1,v2)
    else:
        vysledok = solve(x,y,case)



    print("Case #{}: {}".format(test, vysledok))

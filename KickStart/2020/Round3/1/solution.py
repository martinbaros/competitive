t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    pocet = 0
    posledne = 0
    for q in range(case.count(c)):
        prve = case[posledne:].index(c)+posledne
        je = True
        for l in range(1,c):
            if je and (prve+l < len(case)):
                if case[prve+l] != c-l:
                    je = False
            else:
                je = False
        posledne = prve+1
        if je:
            pocet+=1
    print("Case #{}: {}".format(i, pocet))


t = int(input())  # read a line with a single integer
for prip in range(1, t+1):
    r =  int(input())
    case = []
    for q in range(r):
        case.append([int(s) for s in input().split(" ")])
    all_diags = []
    for i in range(r):
        j = 0
        aktualna = 0
        while i < r and j < r:
            aktualna += case[j][i]
            i+=1
            j+=1
        all_diags.append(aktualna)
    for j in range(r):
        i = 0
        aktualna = 0
        while i < r and j < r:
            aktualna += case[j][i]
            i+=1
            j+=1
        all_diags.append(aktualna)
    print("Case #{}: {}".format(prip, max(all_diags)))

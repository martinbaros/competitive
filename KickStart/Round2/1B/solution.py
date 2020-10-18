t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n = int(input())
    case = [int(s) for s in input().split(" ")]
    vysledok = 0
    for q in range(1,n-1):
        if case[q] > case[q-1] and case[q] > case[q+1]:
            vysledok += 1

    print("Case #{}: {}".format(i, vysledok))

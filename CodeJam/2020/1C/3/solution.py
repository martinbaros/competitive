t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    N, D = [int(s) for s in input().split(" ")]
    slices = [int(s) for s in input().split(" ")]
    vysledok = 1000
    if D == 2:
        for slice in slices:
            if slices.count(slice) > 1:
                vysledok = 0
            else:
                if vysledok > 1:
                    vysledok = 1
    elif D == 3:
        for slice in slices:
            if slices.count(slice) > 2:
                vysledok = 0
            elif slices.count(slice) == 2:
                if slice != max(slices):
                    if vysledok > 1:
                        vysledok = 1
                else:
                    if vysledok > 2:
                        vysledok = 2
            else:
                if vysledok > 2:
                    vysledok = 2
                for op in slices:
                    if op == slice*2:
                        vysledok = 1
    else:
        vysledok = 12
    print("Case #{}: {}".format(i, vysledok))

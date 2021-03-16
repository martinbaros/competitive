def najvyssi(c, hranica):
    for i in range(hranica):
        if (hranica-i)%c==0:
            return hranica-i

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n, d = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    vysledok = False
    aktualny_d = d
    for c in reversed(case):
        aktualny_d = najvyssi(c,aktualny_d)

    print("Case #{}: {}".format(i, aktualny_d))

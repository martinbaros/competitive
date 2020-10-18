t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n, b = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    case.sort()
    mozne = 0
    for dom in case:
        if b -dom >= 0:
            b -= dom
            mozne += 1
        else:
            break
    print("Case #{}: {}".format(i, mozne))

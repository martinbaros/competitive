def vypust(p):
    if p == "S":
        return "E"
    else:
        return "S"

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    rozmer = int([int(s) for s in input().split(" ")][0] )
    cesta = str([str(s) for s in input().split(" ")][0] )
    nova = ""
    for pismenko in cesta:
        nova += vypust(pismenko)
    print("Case #{}: {}".format(i, nova))

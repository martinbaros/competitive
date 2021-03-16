
p = int(input())
for t in range(p):
    n,k,s = [int(q) for q in input().split()]

    result = min(n+k, n+(k-s)*2)
    print("Case #{0}: {1}".format(t+1,result))

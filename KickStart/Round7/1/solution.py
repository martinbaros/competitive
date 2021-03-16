
p = int(input())
for _ in range(p):
    n,k,s = [int(q) for q in input().split()]

    result = min(n+k, n+(k-s)*2)
    print("Case #{0}: {1}".format(_+1,result))

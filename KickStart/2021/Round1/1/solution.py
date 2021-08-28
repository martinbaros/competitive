
p = int(input())
for t in range(p):
    n,k = [int(q) for q in input().split()]
    s = input()
    pocet = 0
    for i in range(0,n//2):

        if s[i] != s[n-1-i]:
            pocet+=1
    result = abs(k - pocet)
    print("Case #{0}: {1}".format(t+1,result))

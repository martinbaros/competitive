
p = int(input())
for test_case in range(p):
    n = int(input())
    s = input()
    vysledok=[]
    start = 1
    posledne_p = s[0]
    for i in range(0,n):
        if posledne_p<s[i]:
            start+=1
        else:
            start=1
        posledne_p=s[i]
        vysledok.append(start)
    result = " ".join[int(s) for s in vysledok])
    print("Case #{0}: {1}".format(test_case+1,result))

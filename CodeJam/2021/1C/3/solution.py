p = int(input())
for test_case in range(p):
    n, = int(input())
    a = s**(1/2)
    ind = (binarySearch(0, len(primes) - 1, a));
    while ind>=0 :
        if (len(primes) <= ind+1 ):
            ind -= 1
            continue
        v = primes[ind] * primes[ind+1]
        if  v > s:
            ind-=1
        else:
            result = v
            break
    print("Case #{0}: {1}".format(test_case+1,result))

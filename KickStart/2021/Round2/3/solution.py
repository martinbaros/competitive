



MAX = 10000;
primes = [];
def Sieve():
    n = MAX;
    nNew = int(n**(1/2));
    marked = [0] * (int(n / 2 + 500));
    for i in range(1, int((nNew - 1) / 2) + 1):
        for j in range(((i * (i + 1)) << 1),
                        (int(n / 2) + 1), (2 * i + 1)):
            marked[j] = 1;

    primes.append(2);
    for i in range(1, int(n / 2) + 1):
        if (marked[i] == 0):
            primes.append(2 * i + 1);

def binarySearch(left, right, n):
    if (left <= right):
        mid = int((left + right) / 2);
        if (mid == 0 or mid == len(primes) - 1):
            return mid;
        if (primes[mid] == n):
            return mid;
        if (primes[mid] < n and primes[mid + 1] > n):
            return mid;
        if (n < primes[mid]):
            return binarySearch(left, mid - 1, n);
        else:
            return binarySearch(mid + 1, right, n);
    return 0;

Sieve();
p = int(input())
for test_case in range(p):
    s = int(input())
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

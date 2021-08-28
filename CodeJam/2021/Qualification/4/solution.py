import sys

def solve(a, b):
    najdene = 0
    for riesena in riesim:
        pripad = {riesena}
        for k in riesena:
            if k not in pripad:
                
        if najdene == 2:
            break

    m = (a + b) // 2
    print(m)
    sys.stdout.flush()
    s = int(input())
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
    else:
        b = m - 1
    solve(a, b)

T,N,Q = [int(s) for s in input().split(" ")]
for _ in range(T):
    if N != 10:
        for i in range(N):
            print(i+1, end=" ")
        print()
    else:
        riesim  = {i+1 for i in range(N)}
        finalny = [0]*N
        solve()

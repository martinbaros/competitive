def ries(seq,chyba):
    a,b,c,d = 0,0,0,0
    A,B,C,D = seq.copy(),seq.copy(),seq.copy(),seq.copy()
    #1
    last="A"
    h = A[0]
    A.pop(0)
    cc = False
    while (not cc) and (len(A)>0):
        if last == "D":
            if A[0] > h:
                cc = True
                a = len(A)
            elif A[0] == h:
                last="D"
                A.pop(0)
            else:
                last="C"
                h = A[0]
                A.pop(0)
        elif last == "A":
            if A[0] < h:
                cc = True
                a = len(A)
            elif A[0] == h:
                last="A"
                A.pop(0)
            else:
                last="B"
                h = A[0]
                A.pop(0)
        elif last == "B":
            if A[0] > h:
                last="C"
                h = A[0]
                A.pop(0)
            elif A[0] == h:
                last="B"
                A.pop(0)
            else:
                last="A"
                h = A[0]
                A.pop(0)
        elif last == "C":
            if A[0] > h:
                last="D"
                h = A[0]
                A.pop(0)
            elif A[0] == h:
                last="C"
                A.pop(0)
            else:
                last="B"
                h = A[0]
                A.pop(0)

    #2
    last="B"
    h = B[0]
    B.pop(0)
    cc = False
    while (not cc) and (len(B)>0):
        if last == "D":
            if B[0] > h:
                cc = True
                b = len(B)
            elif B[0] == h:
                last="D"
                B.pop(0)
            else:
                last="C"
                h = B[0]
                B.pop(0)
        elif last == "A":
            if B[0] < h:
                cc = True
                b = len(B)
            elif B[0] == h:
                last="A"
                B.pop(0)
            else:
                last="B"
                h = B[0]
                B.pop(0)
        elif last == "B":
            if B[0] > h:
                last="C"
                h = B[0]
                B.pop(0)
            elif B[0] == h:
                last="B"
                B.pop(0)
            else:
                last="A"
                h = B[0]
                B.pop(0)
        elif last == "C":
            if B[0] > h:
                last="D"
                h = B[0]
                B.pop(0)
            elif B[0] == h:
                last="C"
                B.pop(0)
            else:
                last="B"
                h = B[0]
                B.pop(0)
    #3
    last="C"
    h = C[0]
    C.pop(0)
    cc = False
    while (not cc) and (len(C)>0):
        if last == "D":
            if C[0] > h:
                cc = True
                c = len(C)
            elif C[0] == h:
                last="D"
                C.pop(0)
            else:
                last="C"
                h = C[0]
                C.pop(0)
        elif last == "A":
            if C[0] < h:
                cc = True
                c = len(C)
            elif C[0] == h:
                last="A"
                C.pop(0)
            else:
                last="B"
                h = C[0]
                C.pop(0)
        elif last == "B":
            if C[0] > h:
                last="C"
                h = C[0]
                C.pop(0)
            elif C[0] == h:
                last="B"
                C.pop(0)
            else:
                last="A"
                h = C[0]
                C.pop(0)
        elif last == "C":
            if C[0] > h:
                last="D"
                h = C[0]
                C.pop(0)
            elif C[0] == h:
                last="C"
                C.pop(0)
            else:
                last="B"
                h = C[0]
                C.pop(0)
    #4
    last="D"
    h = D[0]
    D.pop(0)
    cc = False
    while (not cc) and (len(D)>0):
        if last == "D":
            if D[0] > h:
                cc = True
                d = len(D)
            elif D[0] == h:
                last="D"
                D.pop(0)
            else:
                last="C"
                h = D[0]
                D.pop(0)
        elif last == "A":
            if D[0] < h:
                cc = True
                d = len(D)
            elif D[0] == h:
                last="A"
                D.pop(0)
            else:
                last="B"
                h = D[0]
                D.pop(0)
        elif last == "B":
            if D[0] > h:
                last="C"
                h = D[0]
                D.pop(0)
            elif D[0] == h:
                last="B"
                D.pop(0)
            else:
                last="A"
                h = D[0]
                D.pop(0)
        elif last == "C":
            if D[0] > h:
                last="D"
                h = D[0]
                D.pop(0)
            elif D[0] == h:
                last="C"
                D.pop(0)
            else:
                last="B"
                h = D[0]
                D.pop(0)

    vyhral = min(a,b,c,d)
    if vyhral != 0:
        chyba+=1
        # if vyhral == a:
        #     chyba = ries(A,chyba)
        # elif vyhral == b:
        #     chyba = ries(B,chyba)
        # elif vyhral == c:
        #     chyba = ries(C,chyba)
        # elif vyhral == d:
        #     chyba = ries(D,chyba)

        chyba_a = ries(A,chyba)
        chyba_b = ries(B,chyba)
        chyba_c = ries(C,chyba)
        chyba_d = ries(D,chyba)
        chyba = min(chyba_a,chyba_b,chyba_c,chyba_d)

    return chyba


t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    r =  int(input())
    case = [int(s) for s in input().split(" ")]
    chyba = ries(case,0)

    print("Case #{}: {}".format(i, chyba))

def solve(r,k,s,case):
    poloha = k
    done = set([])
    postupnost = [k]
    all = False
    for i in range(r):
        if all:
            break

        #hladanie l
        #print(done)
        L = -1
        aktual_l = poloha - 2
        #print(aktual_l)
        while( ( aktual_l >= 0 )):
            if aktual_l in done:
                aktual_l -= 1
            else:
                L = case[aktual_l]
                break
        #print(aktual_l)
        #hladanie R
        R = -1
        aktual_r = poloha - 1
        #print(aktual_r)
        while( ( aktual_r <= r-2 )):
            if (aktual_r in done):
                aktual_r += 1
            else:
                R = case[aktual_r]
                break
        #print(aktual_r)
        #print(L,R,poloha)
        if (R<0 and L<0):
            all=True
        elif (R<0 or L<0):
            if R > L:
                poloha = aktual_r+2
                postupnost.append(poloha)
                done.add(aktual_r)
            else:
                poloha = aktual_l+1
                postupnost.append(poloha)
                done.add(aktual_l)

        else:
            pohyb = False
            if (R >= 0) and (R < L):
                poloha = aktual_r+2
                postupnost.append(poloha)
                done.add(aktual_r)
                pohyb = True
            if not pohyb:
                if (L >= 0) and (L < R):
                    poloha = aktual_l+1
                    postupnost.append(poloha)
                    done.add(aktual_l)
    return postupnost






t = int(input())  # read a line with a single integer
for q in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    already = {}
    vysledky = []
    for qu in range(1,c+1):
        k,s = [int(s) for s in input().split(" ")]
        #print(k,s,case)
        if k not in already:
            #print("ide")
            p = solve(r,k,s,case)
            already[k] = p
        else:
            p = already[k]
        vys = p[s-1]
        vysledky.append(str(vys))

    final = " ".join(vysledky)
    print("Case #{}: {}".format(q, final))

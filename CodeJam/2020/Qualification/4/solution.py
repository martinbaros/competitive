
t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    if k%n != 0:
        sprava = "IMPOSSIBLE"
    else:
        sprava = "POSSIBLE"

    print("Case #{}: {}".format(i, sprava))
    if sprava == "POSSIBLE":
        zaciatok = k//n
        aktualne = 2
        while 1:
            riadok = []
            nove = aktualne
            while 1:
                riadok.append(nove)
                nove -= 1
                if nove < 1:
                    nove = n
                if aktualne == nove:
                    break

            prepis = ""
            a = 1
            for cislo in riadok:
                prepis += str(cislo)
                if a < len(riadok):
                    prepis += " "
                a+=1
            print(prepis)
            aktualne+=1
            if aktualne > n:
                aktualne = 1
            if aktualne == zaciatok:
                break


t = int(input())
for test in range(1,t+1):
    s = str(input())
    dlzka = len(s)
    i = 0
    counter = 0
    poloha_kick = []
    while i < dlzka:
        if s[i] == "K":
            if s[i:i+4] == "KICK":
                poloha_kick.append(i)
                i+=3
        i+=1

    poloha_start = []
    k = 0
    while k < dlzka:
        if s[k] == "S":
            if s[k:k+5] == "START":
                poloha_start.append(k)
                k+=4
        k+=1
    for kick in poloha_kick:
        for start in poloha_start:
            if kick < start:
                counter+=1




    print("Case #{}: {}".format(test,counter))

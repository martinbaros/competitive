def kontrola(w,h):
    if w>10**9:
        w -= 10**9
    if h>10**9:
        h -= 10**9
    if w<1:
        w += 10**9
    if h<1:
        h += 10**9
    return (w,h)

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    case = str(input())
    poz  = 0
    w,h = 1,1
    while case.count("(") !=0:
        poz = case.find("(")-1
        if ord(case[poz])<65:
            opakuj = int(case[poz])
            kde = poz+2
            cast = case[poz:kde]
            while cast.count("(") != cast.count(")"):
                kde+=1
                cast = case[poz:kde]
            sekvencia = case[poz+2:kde-1]
            pridat = ""
            for numero in range(opakuj):
                pridat += sekvencia
            case = case[:poz]+pridat+case[kde:]
    h= 1+case.count("S")-case.count("N")
    w = 1+case.count("E")-case.count("W")
    w,h = kontrola(w,h)



    print("Case #{}: {} {}".format(i, w, h))

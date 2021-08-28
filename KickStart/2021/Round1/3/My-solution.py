

def check_horizontal (x,y,r,c):
    original_x = x
    original_y = y
    if x < r and y < c:
        if checked[x][y]:
            return False, 0
        else:
            checked[x][y] = True
    else:
        return False, 0
    pocet_spravnych = 0
    pocet_h = 1
    while (y<c and x<r) and case[x][y]:
        pocet_h += 1
        hladane = 0
        ajdruhe = False
        if pocet_h % 2 == 0 and pocet_h > 2:
            if pocet_h//2 + x - 1 < r:
                hladane = pocet_h//2
        if pocet_h*2 + x - 1 < r:
            if hladane!=0:
                ajdruhe = True
            hladane = (pocet_h*2)
        this_x = x+1
        pocet_v = 1
        if hladane!=0 :
            while (this_x < r and y < c) and case[this_x][y] and pocet_v+1 <= hladane:
                pocet_v += 1
                if pocet_v == hladane:
                    pocet_spravnych += 1
                if ajdruhe:
                    if pocet_v == pocet_h//2:
                        pocet_spravnych += 1
                this_x += 1
        y += 1
    x = original_x
    y = original_y
    pocet_h = 1
    while (y>=0 and x<r) and case[x][y]:
        pocet_h += 1
        hladane = 0
        ajdruhe = False
        if pocet_h % 2 == 0 and pocet_h > 2:
            hladane = pocet_h//2


        if hladane!=0:
            ajdruhe = True
        hladane = (pocet_h*2)

        this_x = x+1
        pocet_v = 0
        if hladane!=0 :
            while (this_x < r and y >=0) and case[this_x][y] and pocet_v+1 <= hladane:
                pocet_v += 1
                if pocet_v == hladane:
                    pocet_spravnych += 1
                if ajdruhe:
                    if pocet_v == pocet_h//2:
                        pocet_spravnych += 1
                this_x += 1
        y -= 1

    return True, pocet_spravnych

def check_vertical (x,y,r,c):
    original_x = x
    original_y = y
    if x < r and y < c:

        checked[x][y] = True
    else:
        return False, 0

    pocet_spravnych = 0
    pocet_h = 1
    while (y<c and x<r) and case[x][y]:
        pocet_h += 1
        hladane = 0
        ajdruhe = False
        if pocet_h % 2 == 0 and pocet_h > 2:
            if pocet_h//2 + y - 1 < c:
                hladane = pocet_h//2
        if pocet_h*2 + y - 1 < c:
            if hladane!=0:
                ajdruhe = True
            hladane = (pocet_h*2)
        this_x = y+1
        pocet_v = 1
        if hladane!=0 :
            while (this_x < c and x < r) and case[x][this_x] and pocet_v+1 <= hladane:
                pocet_v += 1
                if pocet_v == hladane:
                    pocet_spravnych += 1
                if ajdruhe:
                    if pocet_v == pocet_h//2:
                        pocet_spravnych += 1
                this_x += 1
        x += 1

    x = original_x
    y = original_y
    pocet_h = 1
    while (y<c and x>=0) and case[x][y]:
        pocet_h += 1
        hladane = 0
        ajdruhe = False
        if pocet_h % 2 == 0 and pocet_h > 2:
            hladane = pocet_h//2
        if hladane!=0:
            ajdruhe = True
        hladane = (pocet_h*2)

        this_x = y+1
        pocet_v = 0
        if hladane!=0 :
            while (this_x < c and x >=0) and (case[x][this_x] and pocet_v+1 <= hladane):
                pocet_v += 1
                if pocet_v == hladane:
                    pocet_spravnych += 1
                if ajdruhe:
                    if pocet_v == pocet_h//2:
                        pocet_spravnych += 1
                this_x += 1
        x -= 1
    return True, pocet_spravnych

t = int(input())  # read a line with a single integer
for testcase in range(1, t+1):
    r, c = [int(s) for s in input().split(" ")]
    case = []
    checked = []
    for _ in range(r):
        checked.append([False]*c)
    for k in range(1,r+1):
        case.append([bool(int(s)) for s in input().split(" ")])
    next = []
    next.append([0,0])

    pocet_celkovo = 0
    skoky = [(0,1), (1,0)]
    while next != []:
        new = []
        for aktualny in next:
            x = aktualny[0]
            y = aktualny[1]
            for t in skoky:
                vysledne_x = x + t[0]
                vysledne_y = y + t[1]
                valid, v = check_horizontal(vysledne_x, vysledne_y, r, c)
                pocet_celkovo += v
                valid_2, v = check_vertical(vysledne_x, vysledne_y, r, c)
                pocet_celkovo += v
                if (valid or valid_2) and (([vysledne_x,vysledne_y] not in new)):
                    new.append([vysledne_x,vysledne_y])

        next = new


    print("Case #{}: {}".format(testcase, pocet_celkovo))

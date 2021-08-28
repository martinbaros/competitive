t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    x, y = [int(s) for s in input().split(" ")]
    vysledok = ""
    if (x%2 == 0 and y%2 != 0) or (y%2 == 0 and x%2 != 0):
        vysledok = ""
        otocka_x = False
        otocka_y = False
        if x < 0:
            otocka_x = True
        if y < 0:
            otocka_y = True
        pos = True
        x = abs(x)
        y = abs(y)
        if x == 1:
            if y ==0:
                vysledok += "E"
            elif y == 2:
                vysledok += "EN"
            elif y == 4:
                vysledok = "IMPOSSIBLE"
                pos = False
        elif x == 3:
            if y ==0:
                vysledok += "EE"
            if y == 2:
                vysledok += "WNE"
            elif y == 4:
                vysledok += "EEN"
        if y== 1:
            if x ==0:
                vysledok += "N"
            elif x == 2:
                vysledok += "NE"
            elif x == 4:
                vysledok = "IMPOSSIBLE"
                pos = False
        elif y == 3:
            if x ==0:
                vysledok += "NN"
            if x == 2:
                vysledok += "SEN"
            elif x == 4:
                vysledok += "NNE"

        if pos:

            if otocka_x:
                pracovne = ""
                for znak in vysledok:
                    if znak == "W":
                        pracovne += "E"
                    elif znak == "E":
                        pracovne += "W"
                    else:
                        pracovne += znak
                vysledok = pracovne
            if otocka_y:
                pracovne = ""
                for znak in vysledok:
                    if znak == "N":
                        pracovne += "S"
                    elif znak == "S":
                        pracovne += "N"
                    else:
                        pracovne += znak
                vysledok = pracovne

    else:
        vysledok = "IMPOSSIBLE"

    print("Case #{}: {}".format(i, vysledok))

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    x, y, c = [str(s) for s in input().split(" ")]
    x, y = int(x), int(y)
    my_x, my_y = 0,0
    time = len(c)-x
    vysledok = 0
    my_x = x
    chod = True
    if x > len(c):
        vysledok = "IMPOSSIBLE"
        chod = False
    if chod:
        for pql in range(x):
            if c[pql] == "N":
                y+=1
            else:
                y-=1
        ostatok = c[x:]
    #print("Case #{}: {} {} {} {} {}".format(i, x,y,my_x,my_y,ostatok, time))
    while chod:
        if time<=0 and y!=my_y:
            if my_x != x or my_y != y:
                vysledok = "IMPOSSIBLE"
                break
            else:
                vysledok = len(c)-time
                break
        elif my_x == x and my_y == y:
            vysledok = len(c)-time
            break
        else:
            time-=1
            if y > my_y:
                if ostatok[0] == "S":
                    if y-1 != my_y:
                        my_y+=1
                else:
                    my_y+=1
            else:
                if ostatok[0] == "N":
                    if y+1 != my_y:
                        my_y-=1
                else:
                    my_y-=1
            #print(ostatok, y, my_y)
            if ostatok[0] == "S":
                y -= 1
            else:
                y+=1
            ostatok = ostatok[1:]



    print("Case #{}: {}".format(i,vysledok))

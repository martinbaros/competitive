def zhodnot():
    global x,y, vysledok
    if abs(x)%2 !=0:
        if y == 0 and x ==1:
            x+=-1
            vysledok+="E"
        elif y == 0 and x == -1:
            x+=1
            vysledok+="W"
        else:
            if (y//2)%2 != 0:
                if ((x+1)//2)%2 ==0:
                    x+=1
                    vysledok+="W"
                else:
                    x+=-1
                    vysledok+="E"
            else:
                if ((x+1)//2)%2 !=0:
                    x+=1
                    vysledok+="W"
                else:
                    x+=-1
                    vysledok+="E"
    else:
        if x == 0 and y == 1:
            y+=-1
            vysledok+="N"
        elif x == 0 and y==-1:
            y+=1
            vysledok+="S"
        else:
            if (x//2)%2 != 0:
                if ((y+1)//2)%2 ==0:
                    y+=1
                    vysledok+="S"
                else:
                    y+=-1
                    vysledok+="N"
            else:
                if ((y+1)//2)%2 !=0:
                    y+=1
                    vysledok+="S"
                else:
                    y+=-1
                    vysledok+="N"

t = int(input())  # read a line with a single integer
dvojice = [(3,0),(-2,-3),(3,0),(-2,-3)]
for i in range(1, t+1):
    x,y = [int(s) for s in input().split(" ")]
    vysledok = ""
    if (x%2 == 0 and y%2 != 0) or (y%2 == 0 and x%2 != 0):
        while 1:
            zhodnot()
            if x==0 and y==0:
                break
            else:
                x = x//2
                y = y//2
    else:
        vysledok = "IMPOSSIBLE"

    print("Case #{}: {}".format(i, vysledok))

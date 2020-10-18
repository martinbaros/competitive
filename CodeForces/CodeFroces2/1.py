
t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    p = int(input())
    l = [int(s) for s in input().split(" ")]
    check = False
    for q in range(p-2):
        if not check:
            for qq in range(q+1,p-1):
                if not check:
                    for qqq in range(qq+1,p):
                        if not check:
                            x,y,z = l[q],l[qq],l[qqq]
                            if x==y and y==z and z==x:
                                check = True
                            else:
                                vsetky = True
                                if x + y <= z:
                                    vsetky = False
                                if y + z <= x:
                                    vsetky = False
                                if x + z <= y:
                                    vsetky = False
                                if x == 0 or y == 0 or z == 0:
                                    vsetky = False
                                if vsetky:
                                    check = True
    if check:
        print("{} {} {}".format(x,y,z))
    else:
        print("{}".format(-1))

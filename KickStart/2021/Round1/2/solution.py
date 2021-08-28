

t = int(input())  # read a line with a single integer
for prip in range(1, t+1):
    grid = []
    maximum_x, maximum_y = [int(s) for s in input().split(" ")]
    for _ in range(maximum_x):
        grid.append([int(s) for s in input().split(" ")])

    next = []
    next.append([0,0,False])

    pocet_celkovo = 0
    skoky = [(0,1), (1,0)]
    while next != []:
        new = []
        for aktualny in next:
            x = aktualny[0]
            y = aktualny[1]
            special = aktualny[2]
            for t in skoky:
                vysledne_x = x + t[0]
                vysledne_y = y + t[1]
                together = 0
                valid = False
                changed = False
                if (vysledne_x >=0 and vysledne_x <=maximum_x-1) and (vysledne_y>= 0 and vysledne_y<=maximum_y-1):
                    valid = True
                    if (vysledne_x >=0 and vysledne_x <=maximum_x-1) and (vysledne_y>= 0 and vysledne_y<=maximum_y-2):
                        if grid[vysledne_x][vysledne_y+1] - grid[vysledne_x][vysledne_y] > 1 :
                            together += (grid[vysledne_x][vysledne_y+1] - grid[vysledne_x][vysledne_y] -1)
                            grid[vysledne_x][vysledne_y] = grid[vysledne_x][vysledne_y+1]-1
                            changed = True

                    if (vysledne_x >=0 and vysledne_x <=maximum_x-1) and (vysledne_y >= 1 and vysledne_y<=maximum_y-1):
                        if grid[vysledne_x][vysledne_y-1] - grid[vysledne_x][vysledne_y] > 1 :
                            together +=( grid[vysledne_x][vysledne_y-1] - grid[vysledne_x][vysledne_y] -1)
                            grid[vysledne_x][vysledne_y] = grid[vysledne_x][vysledne_y-1]-1
                            changed = True

                    if (vysledne_x>=0 and vysledne_x <= maximum_x-2) and (vysledne_y >= 0 and vysledne_y<=maximum_y-1):
                        if grid[vysledne_x+1][vysledne_y] - grid[vysledne_x][vysledne_y] > 1 :
                            together +=( grid[vysledne_x+1][vysledne_y] - grid[vysledne_x][vysledne_y] -1)
                            grid[vysledne_x][vysledne_y] = grid[vysledne_x+1][vysledne_y]-1
                            changed = True

                    if (vysledne_x>=1 and vysledne_x <=maximum_x-1) and (vysledne_y>= 0 and vysledne_y<=maximum_y-1):
                        if grid[vysledne_x-1][vysledne_y] - grid[vysledne_x][vysledne_y] > 1 :
                            together +=( grid[vysledne_x-1][vysledne_y] - grid[vysledne_x][vysledne_y] -1)
                            grid[vysledne_x][vysledne_y] = grid[vysledne_x-1][vysledne_y]-1
                            changed = True


                if valid and (([vysledne_x,vysledne_y] not in new) and (not special)):
                    new.append([vysledne_x,vysledne_y, False])
                if changed:
                    new.append([vysledne_x,vysledne_y-2,True])
                    new.append([vysledne_x-2,vysledne_y,True])
                pocet_celkovo += together
        next = new

    v =  pocet_celkovo
    print("Case #{}: {}".format(prip, v))

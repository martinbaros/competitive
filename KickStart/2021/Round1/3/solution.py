T = int(input())


def najdi_riadkove(grid,r,s,C):
    out = []
    for j in range(s+1, C):
        if grid[r][j] == 1:
            out.append([s,j,j-s+1])
        else:
            break
    if s>0:
        for j in reversed(range(0, s)):
            if grid[r][j] == 1:
                out.append([s,j,s-j+1])
            else:
                break
    return out

def najdi_stlpcove(grid,r,s,R):
    out = []
    for i in range(r+1, R):
        if grid[i][s] == 1:
            out.append([r,i,i-r+1])
        else:
            break
    if r>0:
        for i in reversed(range(0, r)):
            if grid[i][s] == 1:
                out.append([r,i,r-i+1])
            else:
                break
    return out

for ind in range(T):
    [R, C] = [int(x) for x in input().split()]

    grid = []

    for i in range(R):
        grid.append([int(x) for x in input().split()])

    vysledok = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                vodorovne = najdi_riadkove(grid,i,j,C)
                zvisle = najdi_stlpcove(grid,i,j,R)

                for jedno in vodorovne:
                    vacsia = jedno[2]*2
                    if jedno[2]%2 == 0:
                        mensia = jedno[2]//2
                        for druhe in zvisle:
                            if druhe[2] == mensia:
                                vysledok += 1
                            if druhe[2] == vacsia:
                                vysledok += 1
                    else:
                        for druhe in zvisle:
                            if druhe[2] == vacsia:
                                vysledok += 1
    print('Case #' + str(ind+1)+ ': ' +str(vysledok))

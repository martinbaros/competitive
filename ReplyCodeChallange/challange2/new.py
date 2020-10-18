#T the number of test cases to solve
s = open("output.txt", "w")
all = []
with open("input-scheduler-facc.txt","r") as f:
    for line in f:
        line = line.strip()
        line = line.split(" ")
        all.append(line)

def over():
    global poz, end, smer_x, smer_y, special_y
    if poz[0] < end[0]:
        smer_x = True
    elif poz[0] > end[0]:
         smer_x = False

    if poz[1] < end[1]:
        smer_y = True
    elif poz[1] > end[1]:
         smer_y = False
    else:
        special_y = True


t = int(all[0][0])
print(t)
actual = 1
case_n = 1

while actual < len(all):
    #case-starting

    n = int(all[actual][0])
    m = int(all[actual][1])
    x = 0
    y = 0
    vsetky = []
    for i in range(n):
        y += 1
        x = 0
        actual+=1
        p = all[actual][0]
        for pis in p:
            x+=1
            if x%2 ==0:
                q = 1
            else:
                q= 0
            if pis == "S":
                start = [x,y,q]
            if pis == "D":
                end = [x,y,q]
            k = pis
            vsetky.append([x,y,q,k])


    poz = [3,1,0]
    end = [4,1,1]
    over()
    if poz[2] == 0 and poz[0]%2!=0 and poz[1]%2!=0:
        if special_y and smer_x:
            poz = [poz[0],poz[1],1]
        elif (not smer_y) and smer_x:
            poz = [poz[0]+1,poz[1]-1,1]
        elif smer_y and smer_x:
            poz = [poz[0]+1,poz[1]+1,0]
        elif (not smer_y) and (not smer_x):
            poz = [poz[0]-1,poz[1],0]
        elif smer_y and (not smer_x):
            poz = [poz[0]-1,poz[1],1]


    print(poz)
    #while poz != end:


    actual+=1
    case_n+=1

s.close()

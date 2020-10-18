file=open("subor.txt","r")
zoznam=[]
zoznam2=[]
poc=0
zoznam_teamov=[]
zoznam3=[]
text=""
for i in file:
    i=i.strip().split()
    if poc ==0:
        case_number=i[0]
    elif poc==1:
        N=int(i[0])
        L=int(i[1])
        for h in range(1,L+1):
            zoznam_teamov.append(str(h))

    else:
        if str(i[1]) in zoznam_teamov:
            zoznam_teamov.remove(str(i[1]))
        slv={"timestamp":int(i[0]),
             "team_id":str(i[1]),
             "problem_id": int(i[2]),
             "input_id": int(i[3]),
             "scored":int(i[4]),
             "points":0,
             "penalty":0,
             }
        zoznam.append(slv)
    poc+=1

for i in zoznam:
    if i["scored"]==1:
        i["points"]=100*i["input_id"]
        i["penalty"]=int(i["timestamp"])

for i in zoznam:
    if i["team_id"] in zoznam2:
        index=zoznam2.index(i["team_id"])
        a=zoznam2[index+1]
        zoznam2.insert((index+1),((i["points"])+a-i["penalty"])+0.0000000000000000001)
        zoznam2.remove(zoznam2[index ])




    else:
        zoznam2.append(i["team_id"])
        zoznam2.append(i["points"]-i["penalty"]+1)


for i in zoznam2:
    if zoznam2.index(i)%2==1:
        zoznam3.append(i)

zoznam3.sort()
zoznam3.reverse()

for i in zoznam3:
    text+=str(zoznam2[zoznam2.index(i)-1])+" "
for i in zoznam_teamov:
    text+=str(i)+" "
print("Case #"+str(case_number)+": "+text)

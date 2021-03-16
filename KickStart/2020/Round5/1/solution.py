
t = int(input())
for test in range(1,t+1):
    p=int(input())

    l = [int(s) for s in input().split(" ")]
    longest = 0
    for k in range(p-1):
        ak=2
        cr= l[k] - l[k+1]
        last = l[k+1]
        #print(cr, "Hey tu", l[k+1] , l[k])
        for q in range(p-k-2):
            #print(l[q+k+2])
            if l[q+k+2] == last -cr:
                ak+=1
                last = l[q+k+2]
            else:
                break


        if ak>longest:
            longest=ak
    print("Case #{}: {}".format(test,longest))

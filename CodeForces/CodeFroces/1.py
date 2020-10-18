def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    l, r = [int(s) for s in input().split(" ")]
    x = l
    y = x+1
    check = False
    while not check and (x < y and y<=r):
        # print("HERE")
        # print(lcm(x,y),x,y)
        # print("DONE")
        if lcm(x,y) >= l and lcm(x,y) <= r:
            check = True
        else:
            if y+1 > r:
                x+=1
                y = x+1
            else:
                y+=1
    #print(check)
    if not check:
        x,y = -1, -1



    print("{} {}".format(x,y))

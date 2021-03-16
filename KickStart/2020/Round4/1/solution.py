t = int(input())  # read a line with a single integer
for q in range(1, t+1):
    r = int(input())
    case = [int(s) for s in input().split(" ")]
    gb = 0
    maxo = -1
    for i in range(r):
        if i < r-1:
            if case[i] > maxo:
                maxo = case[i]
                if case[i] > case[i+1]:
                    gb+=1
        else:
            if case[i] > maxo:
                gb+=1




    print("Case #{}: {}".format(q, gb))

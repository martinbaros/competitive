t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n, q = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    score = []
    for k in range(1,q+1):
        line = [str(s) for s in input().split(" ")]
        if line[0] == "Q":
            sub = case[int(line[1])-1:int(line[2])]
            mini = 0
            for A in range(len(sub)):
                mini += ((-1)**A)*sub[A]*(A+1)
            score.append(mini)
        elif line[0]=="U":
            case[int(line[1])-1] = int(line[2])

    print("Case #{}: {}".format(i, sum(score)))

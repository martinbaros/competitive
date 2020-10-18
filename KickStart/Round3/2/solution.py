
t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n = int(input())
    case = [int(s) for s in input().split(" ")]
    pocet = 0
    for k in range(n):
        for ak in range(n-k):
            number = sum(case[k:ak+k+1])
            if number > 0:
                z = number**(1/2)
                if int(z + 0.5) ** 2 == number:
                    pocet+=1
            elif number == 0:
                pocet+=1


    print("Case #{}: {}".format(i, pocet))

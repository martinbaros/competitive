t = int(input())
for test in range(1, t+1):
    n = int(input())
    case = [str(s) for s in input().split(" ")]
    operacie = 0
    for i in range(1,n):
        A = case[i-1]
        B = case[i]
        if int(A) < int(B):
            continue
        elif len(A) == len(B):
            operacie += 1
            case[i] = (B+"0")
        else:
            k = len(A) - len(B)
            B_p = B + ("0"*k)
            if int(A) < int(B_p):
                operacie += k
                case[i] = (B_p)
                continue
            else:    
                B_p = B + ("9"*k)
                if int(A) < int(B_p):
                    operacie += k
                    case[i] = str(int(A)+1)
                    continue
                B_p = B + ("0"*(k+1))
                operacie += k+1
                case[i] = (B_p)



    #print(case)
    print("Case #{}: {}".format(test, operacie))

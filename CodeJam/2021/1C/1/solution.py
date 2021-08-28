def get_number(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 0
    else:
        pocet = n-2
        return (pocet // 2) +1

p = int(input())
for test_case in range(p):
    n,k = [int(s) for s in input().split(" ")]
    case = [int(s) for s in input().split(" ")]
    case.append(k+1)
    case.sort()
    largest, second_largest = -5,-3
    for i in range(len(case)-1):
        inp = case[i+1] - case[i]
        if inp > second_largest:
            if inp > largest:
                if i+1 == len(case)-1:
                    inp = (inp-1) * 2
                second_largest = largest
                largest = inp
            else:
                if i+1 == len(case)-1:
                    inp = (inp-1) * 2
                second_largest = inp
    celkovo = get_number(largest) + get_number(second_largest)
    if celkovo <= 0:
        celkovo = 0
    print("Case #{0}: {1}".format(test_case+1,round(celkovo/k, 6)))

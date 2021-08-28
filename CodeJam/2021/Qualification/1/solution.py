def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]


t = int(input())
for test in range(1, t+1):
    #n = int(input())
    dlzka = 0
    case = [int(s) for s in input().split(" ")]
    n = len(case)
    for i in range(n):
        minimum = case[i]
        j = i
        for k in range(i+1,n):
            if case[k] < minimum:
                minimum = case[k]
                j = k
        if i!= n-1:
            dlzka += (j-i+1)
        reverse(case, i, j)




    print("Case #{}: {}".format(test, dlzka))

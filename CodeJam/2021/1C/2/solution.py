def maxArithmeticSubarray(array,N,start,stop):
    maxLen = 0;
    for i in range(0,N-1):
        j = i;
        k_j = 0
        q_j=i
        qa_j = i
        common_difference = array[i+1] - array[i];
        while(j<N-1):
            if (array[j + 1] - array[j] == common_difference):
                j+=1
            else:
                k_j = j
                kopia = array.copy()
                kopia[j + 1] = kopia[j] + common_difference
                k_j+=1
                while ((k_j < N-1) and (kopia[k_j + 1] - kopia[k_j] == common_difference)):
                    k_j+=1
                break
        if (i<N-2):
            q_j = i
            common_difference2 = array[q_j+2] - array[q_j];
            kopia = array.copy()
            kopia[q_j + 1] = kopia[q_j] + common_difference2
            while(q_j<N-1) and (kopia[q_j + 1] - kopia[q_j] == common_difference2):
                    q_j+=1

            qa_j = i
            common_difference3 = array[qa_j+2] - array[qa_j+1];
            kopia2 = array.copy()
            kopia2[qa_j] = kopia2[qa_j+1] - common_difference3
            while(qa_j<N-1) and (kopia2[qa_j + 1] - kopia2[qa_j] == common_difference3):
                    qa_j+=1

        max_j = max(k_j, j, q_j, qa_j)
        maxLen = max(maxLen, max_j - i + 1)
        i = max(i + 1, max_j)
    return maxLen;


def seg(a, n):

    l = [0] * n
    r = [0] * (n + 1)
    ans = 0

    # calculating the l array.
    l[0] = 1
    for i in range(1, n):
        if (a[i] > a[i - 1]):
            l[i] = l[i - 1] + 1
            ans = max(ans, l[i])
        else:
            l[i] = 1

    if (ans != n):
        ans += 1

    # calculating the
    # r array.
    r[n] = 0
    for i in range(n - 1,
                   -1, -1):
        if (a[i - 1] < a[i]):
            r[i] = r[i + 1] + 1
        else:
            r[i] = 1

    # Updating the answer.
    for i in range(n - 2,
                   0, -1):
        if (a[i + 1] -
            a[i - 1] > 1):
            ans = max(ans, l[i - 1] +
                      r[i + 1] + 1)

    return max(ans, r[0])


p = int(input())
for test_case in range(p):
    N = int(input())
    case = [int(q) for q in input().split()]

    result = seg(case,N)
    print("Case #{0}: {1}".format(test_case+1,result))

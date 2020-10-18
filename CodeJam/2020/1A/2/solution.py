t = int(input())  # read a line with a single integer
for p in range(1, t+1):
    n = int(input())
    cases = []
    for q in range(1,n+1):
        cases.append(str(input()))
    pozicne = {}
    dlzky = []
    for case in cases:
        pozicne[case] = case.index("*")
        dlzky.append(len(case))
    zoradene = []
    for x in sorted(pozicne, key = pozicne.get, reverse = True):
        zoradene.append(x)

    final = cases[dlzky.index(max(dlzky))][1:]
    koniec = len(final)-1
    zle = False
    for case in cases:
        for i in range(len(case)-1):
            if not zle:
                if case[len(case)-1-i] != final[koniec-i]:
                    zle = True
                    final = "*"
    if len(final) >= 10**4:
        final = "*"

    #for case in zoradene:
        #
        # docasne = ""
        # if case.index("*") == len(case)-1:
        #     case = case[:len(case)-1]
        #     print(len(case)-1, case)
        #     islo = False
        #     pozmenene = False
        #     for k in range(len(final)):
        #         if k < len(case):
        #             if final[k] == case[k]:
        #                 docasne += final[k]
        #             else:
        #                 pozmenene = True
        #                 kde = k+1
        #         islo = True
        #
        #     if islo == False:
        #         k = 0
        #     else:
        #         k += 1
        #     print(k)
        #
        #     if pozmenene:
        #         docasne += case[kde:]
        #     else:
        #         if k < len(case):
        #             print("preslo", case[k:])
        #             docasne += case[k:]
        # final = docasne





    print("Case #{}: {}".format(p, final))

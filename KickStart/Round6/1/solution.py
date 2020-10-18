t = int(input())
for test_case in range(1,t+1):
    n, x = [int(s) for s in input().split(" ")]
    persons = [int(q) for q in input().split(" ")]

    ne = {num:(value//x) for num, value in enumerate(persons, start=1)}
    vysledok = " ".join([str(k) for k in sorted(ne, key=ne.get)])
    print("Case #{}: {}".format(test_case, vysledok))

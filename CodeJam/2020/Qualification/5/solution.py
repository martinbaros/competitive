from sys import stdout

t, b = [int(s) for s in input().split(" ")]
for case_idx in range(t):
    cisla = []
    for k in range(15):
        cislo = ""
        for i in range(10):
            print(i+1)
            stdout.flush()
            cislo+=str(input())
        cisla.append(cislo)

    print(cislo)
    stdout.flush()
    input()

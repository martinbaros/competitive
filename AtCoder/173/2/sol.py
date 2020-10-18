n = int(input())
a,b,c,d = 0,0,0,0
for i in range(n):
    p = str(input())
    if p == "AC":
        a += 1
    elif p == "WA":
        b += 1
    elif p == "TLE":
        c += 1
    elif p == "RE":
        d += 1

print("AC x {}".format(a))
print("WA x {}".format(b))
print("TLE x {}".format(c))
print("RE x {}".format(d))
